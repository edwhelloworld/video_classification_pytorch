import argparse
parser = argparse.ArgumentParser(description="PyTorch implementation of Temporal Segment Networks")
parser.add_argument('--dataset', type=str, default='UCF101', choices=['ucf101', 'hmdb51', 'kinetics'])
parser.add_argument('--modality', type=str, default='RGB', choices=['RGB', 'Flow', 'RGBDiff'])
parser.add_argument('--split', type=int, default=1, choices=[1, 2, 3])
parser.add_argument('--model', type=str, default='i3d', choices=['i3d', 'tsn', 'non_local', 's3d'])
parser.add_argument('--arch', type=str, default="resnet101")
parser.add_argument('--pretrained', action='store_true', default=False)
# For i3d, pretrained on ImageNet and Kinetics
# For tsn, pretrained on ImageNet (just a 2D model)
# For non_local, pretrained on ImageNet. (Inflat 2D kernel to 3D)
# For s3d, load weights of i3d model's pretrained on ImageNet and Kinetics

# ========================= TSN Configs ==========================

parser.add_argument('--num_segments', type=int, default=3)
parser.add_argument('--consensus_type', type=str, default='avg',
                    choices=['avg', 'max', 'topk', 'identity', 'rnn', 'cnn'])
parser.add_argument('--k', type=int, default=3)
parser.add_argument('--dropout', '--do', default=0.5, type=float,
                    metavar='DO', help='dropout ratio (default: 0.5)')
parser.add_argument('--loss_type', type=str, default="nll",
                    choices=['nll'])

# ========================= Learning Configs ==========================
parser.add_argument('--epochs', default=45, type=int, metavar='N',
                    help='number of total epochs to run')
parser.add_argument('--batch-size', default=256, type=int,
                    metavar='N', help='mini-batch size (default: 256)')
parser.add_argument('--lr', '--learning-rate', default=0.001, type=float,
                    metavar='LR', help='initial learning rate')
parser.add_argument('--lr-steps', default=[20, 40], type=float, nargs="+",
                    metavar='LRSteps', help='epochs to decay learning rate by 10')
parser.add_argument('--momentum', default=0.9, type=float, metavar='M',
                    help='momentum')
parser.add_argument('--weight-decay', '--wd', default=5e-4, type=float,
                    metavar='W', help='weight decay (default: 5e-4)')
parser.add_argument('--clip-gradient', '--gd', default=None, type=float,
                    metavar='W', help='gradient norm clipping (default: disabled)')
parser.add_argument('--no_partialbn', '--npb', default=False, action="store_true")

# ========================= Monitor Configs ==========================
parser.add_argument('--visdom-name', default='tsn_01', type=str)
parser.add_argument('--visdom-port', default=8197, type=int)
parser.add_argument('--val-interval', default=5, type=int)

# ========================= Runtime Configs ==========================
parser.add_argument('-j', '--workers', default=0, type=int, metavar='N',
                    help='number of data loading workers (default: 4)')
parser.add_argument('--resume', default='', type=str, metavar='PATH',
                    help='path to latest checkpoint (default: none)')
# parser.add_argument('-e', '--evaluate', dest='evaluate', action='store_true',
#                     help='evaluate model on validation set')
# parser.add_argument('--snapshot_pref', type=str, default="")
# parser.add_argument('--start-epoch', default=0, type=int, metavar='N',
#                     help='manual epoch number (useful on restarts)')
# parser.add_argument('--gpus', nargs='+', type=int, default=None)
# parser.add_argument('--flow_prefix', default="", type=str)








