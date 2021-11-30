""" Tests for env_data.py """

import os
import re
import random
import string
from subprocess import getstatusoutput, getoutput

PRG = 'env_data/env_data.py'
INPUT = 'new_data/test_data.csv'
EXPECTED1 = 'tests/expected/expected1.txt'
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
def test_bad_file():
    """fails on bad input"""

    bad = random_string()
    rv, out = getstatusoutput(f'{PRG} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def run(args, expected_file):
    """ Run test """

    assert os.path.isfile(expected_file)
    expected = open(expected_file).read().rstrip()
    rv, out = getstatusoutput(f'{PRG} {" ".join(args)}')
    data = open('./output/data.csv').read().rstrip()
    assert rv == 0
    assert data == expected


# --------------------------------------------------
def test1():
    """ test """

    run([INPUT], EXPECTED1)
