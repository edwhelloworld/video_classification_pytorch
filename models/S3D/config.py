import torch
from torch.utils.data import DataLoader
import torchvision.transforms as T
import torch.nn as nn

import utils.transforms as ut_transforms 
from pt_dataset.consecutive_dataset import Consecutive
from models.S3D.Inceptionv1_S3D import make_inception_s3d
import main
args = main.args

# 暂时只支持RGB frames 和kinetics数据集

class I3Dscale(object):
    # rescale piexls values in[0, 1] to [-1, 1]
    def __init__(self):
        return

    def __call__(self, data):
        return data*2 - 1.0


train_transforms = T.Compose([
    ut_transforms.GroupScale(256), # resize smaller edge to 256
    ut_transforms.GroupRandomCrop(224), # randomlly crop a 224x224 patch
    ut_transforms.GroupRandomHorizontalFlip(),
    ut_transforms.GroupToTensor(),
    ut_transforms.StackTensor(),
    I3Dscale()
])

# val_transforms = T.Compose([
#     ut_transforms.GroupScale(256),
#     ut_transforms.GroupCenterCrop(224), # full convolution in test time
#     ut_transforms.GroupToTensor(),
#     ut_transforms.StackTensor(),
#     I3Dscale()
# ])

val_transforms = T.Compose([
    ut_transforms.GroupScale(256), # resize smaller edge to 256
    ut_transforms.GroupRandomCrop(224), # randomlly crop a 224x224 patch
    ut_transforms.GroupRandomHorizontalFlip(),
    ut_transforms.GroupToTensor(),
    ut_transforms.StackTensor(),
    I3Dscale()
])


train_dataset = Consecutive(dataset=args.dataset, train=False, transform=train_transforms) #default 64 frames
val_dataset = Consecutive(dataset=args.dataset, train=False, transform=val_transforms)

train_loader = DataLoader(
    train_dataset, batch_size=args.batch_size, 
    shuffle=True, num_workers=args.workers,
    pin_memory=True)

val_loader = DataLoader(
    val_dataset, batch_size=args.batch_size,
    shuffle=True, num_workers=args.workers,
    pin_memory=True
)

num_class = train_dataset.num_classes

model = make_inception_s3d(pretrained=args.pretrained, num_classes=num_class) # only RGB model avaliable right now


model = nn.DataParallel(model)


