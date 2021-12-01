#!/usr/bin/env python3

import os
from shutil import copy2

# --------------------------------------------------
def main():
    """ Reset project folder """

    data = 'output/data.csv'
    data_bak = 'reset/data.csv'
    old_data1 = 'old_data/data_2021_06_22_1520.csv'
    old_data2 = 'old_data/data_2021_06_22_2050.csv'
    new_data1 = 'new_data/data_2021_06_22_1520.csv'
    new_data2 = 'new_data/data_2021_06_22_2050.csv'

    # Move the data files back to new data folder if moved
    if os.path.isfile(old_data1):
        os.rename(old_data1, new_data1)

    if os.path.isfile(old_data2):
        os.rename(old_data2, new_data2)

    # Reset data.csv to original file
    os.remove(data)
    copy2(data_bak, data)

    print('Project folders reset.')
    



# --------------------------------------------------
if __name__ == '__main__':
    main()