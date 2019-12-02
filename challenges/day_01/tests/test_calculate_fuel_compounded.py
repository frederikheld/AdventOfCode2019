import pytest
from ..lib.calculate_fuel import *
from ..lib.calculate_fuel_compounded import *


def test_calculate_fuel_from_mass_compounded():
    assert calculate_fuel_from_mass_compounded(14) == 2
    assert calculate_fuel_from_mass_compounded(1969) == 966
    assert calculate_fuel_from_mass_compounded(100756) == 50346


def test_calculate_compounded_fuel_from_list():
    list1 = """\
14
1969
100756
"""
    assert calculate_total_fuel_from_list(
        list1, calculate_fuel_from_mass_compounded) == (2 + 966 + 50346)
