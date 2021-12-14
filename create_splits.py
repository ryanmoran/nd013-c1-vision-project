import argparse
import glob
import os
import random
from datetime import datetime
import shutil

import numpy as np

from utils import get_module_logger


def split(source, destination):
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.

    args:
        - source [str]: source data directory, contains the processed tf records
        - destination [str]: destination data directory, contains 3 sub folders: train / val / test
    """
    paths = os.listdir(source)
    random.seed(datetime.now())
    random.shuffle(paths)

    splits = {
        os.path.join(destination, 'train'): paths[:75],
        os.path.join(destination, 'val'): paths[75:90],
        os.path.join(destination, 'test'): paths[90:]
    }

    for directory in splits.keys():
        os.makedirs(directory, exist_ok=True)

        for path in splits[directory]:
            src = os.path.join(source, path)
            dst = os.path.join(directory, path)
            print(f'moving {src} to {dst}')
            shutil.move(src, dst)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--source', required=True,
                        help='source data directory')
    parser.add_argument('--destination', required=True,
                        help='destination data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.source, args.destination)
