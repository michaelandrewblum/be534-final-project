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

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='CSV input file')

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


    args = parser.parse_args()

    if os.path.splitext(args.file.name)[1] != '.csv':
        parser.error(f'Input file "{args.file.name}" should be csv file.')

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    infile = args.file.name
    outfile = args.outfile.name
    
    in_fh = open(infile, 'r')
    out_fh = open(outfile, 'a')

    for row in in_fh:
        out_fh.write(row)

    print(f'Data copied to {outfile}.', '\n')

    print('{:<20}{:>7}'.format('Sensor', 'Average'))

    if args.dashboard:

        headers = headers = ["RECORD","batt_volt_Min","PanelT","RH_East_Avg","RH_West_Avg","RH_Center_Avg","AirT_East_Avg","AirT_West_Avg","AirT_Center_Avg","PAR_E_Avg","PAR_W_Avg","PAR_E_Total","PAR_W_Total","Incoming_SW_Avg","Outgoing_SW_Avg","Incoming_LW_Avg","Outgoing_LW_Avg","TargmV_E_Avg","SBTempC_E_Avg","TargTempC_E_Avg","TargmV_W_Avg","SBTempC_W_Avg","TargTempC_W_Avg"]
        avg_list = get_averages(in_fh)
        avg_dict = {}

        for index, header in enumerate(headers):
            avg_dict[header] = avg_list[index]

        print_headers = ["RH_East_Avg","RH_West_Avg","RH_Center_Avg","AirT_East_Avg","AirT_West_Avg","AirT_Center_Avg","PAR_E_Avg","PAR_W_Avg","TargTempC_E_Avg","TargTempC_W_Avg"]
        for header in print_headers:
            print(f'{header:<20}{avg_dict[header]:>7}')

    # Move new input data file into old_data folder.

    Path(infile).rename('old_data/' + os.path.basename(infile))

  


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
                    pass
            row_count += 1.0
    row_count -= 1.0
    col_indexes = col_totals.keys()

    averages = [round(col_totals[id]/row_count,2) for id in col_indexes]

    return averages


# --------------------------------------------------
if __name__ == '__main__':
    main()
