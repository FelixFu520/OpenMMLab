# Copyright (c) OpenMMLab. All rights reserved.
import argparse
import os

from mmengine.config import Config


def parse_args():
    parser = argparse.ArgumentParser(description='Integrate a config')
    parser.add_argument('config', help='train config file path')
    parser.add_argument('save_dir', help='train config file save path')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    # load config
    cfg = Config.fromfile(args.config)
    os.makedirs(args.save_dir, exist_ok=True)
    cfg.dump(os.path.join(args.save_dir, os.path.basename(args.config)))


if __name__ == '__main__':
    main()
