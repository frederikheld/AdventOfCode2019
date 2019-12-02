import pytest
import os

from ..lib.calculate_fuel import calculate_fuel_from_mass
from ..lib.calculate_fuel import calculate_total_fuel_from_list


def test_calculate_fuel_from_mass():
    assert calculate_fuel_from_mass(12) == 2
    assert calculate_fuel_from_mass(14) == 2
    assert calculate_fuel_from_mass(1969) == 654
    assert calculate_fuel_from_mass(100756) == 33583


def test_calculate_total_fuel_from_list():
    list1 = """ \
12
14
1969
"""
    assert calculate_total_fuel_from_list(list1) == 658

    list2 = """\
1969
100756
"""
    assert calculate_total_fuel_from_list(list2) == (654 + 33583)


def test_actual_challenge():
    f = open(
        os.path.dirname(os.path.realpath(__file__)) +
        '/../data/input.txt', 'r'
    )
    list1 = f.read()

    assert calculate_total_fuel_from_list(list1) == 3315383
