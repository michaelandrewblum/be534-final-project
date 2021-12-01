""" Tests for env_data.py """

import os
import re
import random
import string
from subprocess import getstatusoutput, getoutput
from shutil import copy2

PRG = 'env_data/env_data.py'
INPUT1 = 'new_data/data_2021_06_22_1520.csv'
INPUT2 = 'new_data/data_2021_06_22_2050.csv'
INPUTALL = 'new_data/*'
OUTPUT = 'output/data.csv'
EXPECTED1_F = 'tests/expected/expected1_f.txt'
EXPECTED1_S = 'tests/expected/expected1_s.txt'
EXPECTED1_SD = 'tests/expected/expected1_sd.txt'
EXPECTED2_F = 'tests/expected/expected2_f.txt'
EXPECTED2_S = 'tests/expected/expected2_s.txt'
EXPECTED2_SD = 'tests/expected/expected2_sd.txt'
EXPECTED_ALL_F = 'tests/expected/expected_all_f.txt'
EXPECTED_ALL_S = 'tests/expected/expected_all_s.txt'
EXPECTED_ALL_SD = 'tests/expected/expected_all_sd.txt'
DATAFILE = 'output/data.csv'


# --------------------------------------------------
def random_string():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Prints usage """

    for flag in ['', '-h', '--help']:
        out = getoutput(f'{PRG} {flag}')
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_input_file():
    """ fails on bad input file """

    bad = random_string()
    rv, out = getstatusoutput(f'{PRG} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_no_output_file():
    """ fails on no output file """

    assert os.path.isfile(OUTPUT)


# --------------------------------------------------
def run(args, expected_stdout, expected_datafile, tags=''):
    """ Run test """

    tag_fmt = '' if tags == '' else tags + ' '
    # temp_file = "_" + os.path.dirname(DATAFILE)
    copy2(DATAFILE, 'output/temp_data.csv')
    try:
        assert os.path.isfile(expected_stdout)
        expected_std = open(expected_stdout).read().rstrip()
        expected_data = open(expected_datafile).read().rstrip()
        print(f'{PRG} {tags}{" ".join(args)}')
        rv, out = getstatusoutput(f'{PRG} {tag_fmt}{" ".join(args)}')
        data = open(DATAFILE).read().rstrip()
        assert rv == 0
        assert out == expected_std
        assert data == expected_data
    finally:
        os.remove(DATAFILE)
        os.rename('output/temp_data.csv', DATAFILE)


# --------------------------------------------------
def test_print_to_stdout_dashboard_1():
    """ test """

    run([INPUT1], EXPECTED1_SD, EXPECTED1_F, tags='-dr')


# --------------------------------------------------
def test_print_to_stdout_1():
    """ test """

    run([INPUT1], EXPECTED1_S, EXPECTED1_F, tags='-r')


# --------------------------------------------------
def test_print_to_stdout_dashboard_2():
    """ test """

    run([INPUT2], EXPECTED2_SD, EXPECTED2_F, tags='-dr')


# --------------------------------------------------
def test_print_to_stdout_2():
    """ test """

    run([INPUT2], EXPECTED2_S, EXPECTED2_F, tags='-r')


# --------------------------------------------------
def test_print_to_stdout_dashboard_all():
    """ test """

    run([INPUTALL], EXPECTED_ALL_SD, EXPECTED_ALL_F, tags='-dr')


# --------------------------------------------------
def test_print_to_stdout_all():
    """ test """

    run([INPUTALL], EXPECTED_ALL_S, EXPECTED_ALL_F, tags='-r')
