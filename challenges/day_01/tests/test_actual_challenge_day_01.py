import pytest
import os

from ..lib.calculate_fuel import *
from ..lib.calculate_fuel_compounded import *


def test_actual_challenge_day_01_challenge_01():
    f = open(
        os.path.dirname(os.path.realpath(__file__)) +
        '/../input/challenge_01.txt', 'r'
    )
    list1 = f.read()

    assert calculate_total_fuel_from_list(list1) == 3315383


def test_actual_challenge_day_01_challenge_02():
    f = open(
        os.path.dirname(os.path.realpath(__file__)) +
        '/../input/challenge_02.txt', 'r'
    )
    list1 = f.read()

    assert calculate_total_fuel_from_list(
        list1, calculate_fuel_from_mass_compounded) == 4970206


4970206
