#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-11-17
Purpose: Environmental Data Dashboard
"""

import argparse
import csv


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Environmental Data Dashboard',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='CSV input file')

    # parser.add_argument('-a',
    #                     '--arg',
    #                     help='A named string argument',
    #                     metavar='str',
    #                     type=str,
    #                     default='')

    # parser.add_argument('-i',
    #                     '--int',
    #                     help='A named integer argument',
    #                     metavar='int',
    #                     type=int,
    #                     default=0)

    # parser.add_argument('-f',
    #                     '--file',
    #                     help='A readable file',
    #                     metavar='FILE',
    #                     type=argparse.FileType('rt'),
    #                     default=None)

    # parser.add_argument('-o',
    #                     '--on',
    #                     help='A boolean flag',
    #                     action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    with open(args.file.name, 'rt') as csv_fh:
        reader = csv.reader(csv_fh)
        for row in reader:
            print('\t'.join(row))


# --------------------------------------------------
if __name__ == '__main__':
    main()
