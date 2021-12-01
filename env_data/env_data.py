#!/usr/bin/env python3
"""
Author : michaelblum <michaelblum@localhost>
Date   : 2021-11-17
Purpose: Environmental Data Dashboard
"""

import argparse
import os
import csv
from collections import Counter
from pathlib import Path


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Environmental Data Dashboard',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='CSV input file(s)')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILe',
                        type=argparse.FileType('at'),
                        default='output/data.csv',
                        help='CSV input file')

    parser.add_argument('-d',
                        '--dashboard',
                        help='A boolean flag',
                        action='store_true')

    parser.add_argument('-n',
                        '--nottofile',
                        help='A boolean flag',
                        action='store_true')

    parser.add_argument('-r',
                        '--remain',
                        help='A boolean flag',
                        action='store_true')

    args = parser.parse_args()
    for file in args.files:
        if os.path.splitext(file.name)[1] != '.csv':
            parser.error('Error -- All input files should be csv files.')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    outfile = args.outfile.name

    # Sort infiles, which will put them in chronological order
    infiles_sorted = sorted(args.files, key=lambda fh: fh.name)

    if not args.nottofile:
        # Copy contents of input files to output file
        for infile in infiles_sorted:
            in_fh = open(infile.name, 'r')
            out_fh = open(outfile, 'a')

            for row in in_fh:
                out_fh.write(row)

        # Print to stdout what files input and where output
        for infile in infiles_sorted:
            print(f'Data input from {infile.name}.')

        print(f'Data copied to {outfile}.')

    # Get averages for data input in select columns
    if args.dashboard:

        headers = [
            "TIMESTAMP", "RECORD", "batt_volt_Min", "PanelT", "RH_East_Avg",
            "RH_West_Avg", "RH_Center_Avg", "AirT_East_Avg", "AirT_West_Avg",
            "AirT_Center_Avg", "PAR_E_Avg", "PAR_W_Avg", "PAR_E_Total",
            "PAR_W_Total", "Incoming_SW_Avg", "Outgoing_SW_Avg",
            "Incoming_LW_Avg", "Outgoing_LW_Avg", "TargmV_E_Avg",
            "SBTempC_E_Avg", "TargTempC_E_Avg", "TargmV_W_Avg",
            "SBTempC_W_Avg", "TargTempC_W_Avg"
        ]

        headers_to_print = [
            "RH_East_Avg", "RH_West_Avg", "RH_Center_Avg", "AirT_East_Avg",
            "AirT_West_Avg", "AirT_Center_Avg", "PAR_E_Avg", "PAR_W_Avg",
            "TargTempC_E_Avg", "TargTempC_W_Avg"
        ]

        for infile in infiles_sorted:
            print('')
            print('{:20}{:7}'.format('Sensor', 'Average'))
            print('-' * 27)

            avg_list = get_averages(infile)
            avg_dict = {}

            for i, header in enumerate(headers):
                avg_dict[header] = avg_list[i]

            for header in headers_to_print:
                print(f'{header:<20}{avg_dict[header]:>7}')

    # Move new input data file into old_data folder if not remain flag.
    if not args.remain:
        for infile in infiles_sorted:
            Path(infile.name).rename('old_data/' +
                                     os.path.basename(infile.name))


# --------------------------------------------------
def get_averages(fh):
    """ format data dashboard """

    col_totals = Counter()
    with open(fh.name, 'rt') as f:
        reader = csv.reader(f)
        row_count = 0.0
        for row in reader:
            for col_id, col_value in enumerate(row):
                try:
                    n = float(col_value)
                    col_totals[col_id] += n
                except ValueError:
                    col_totals[col_id] = 'N/A'
            row_count += 1.0
    row_count -= 1.0
    col_indexes = col_totals.keys()

    averages = []
    for i in col_indexes:
        try:
            averages.append(round(col_totals[i] / row_count, 2))
        except TypeError:
            averages.append(col_totals[i])

    return averages


# --------------------------------------------------
if __name__ == '__main__':
    main()
