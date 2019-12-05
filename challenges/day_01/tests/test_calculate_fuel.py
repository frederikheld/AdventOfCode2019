import pytest
import os

from challenges.day_01.lib.calculate_fuel import *


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
