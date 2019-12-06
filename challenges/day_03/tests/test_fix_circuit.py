import pytest

from challenges.day_03.lib.fix_circuit import *


def test_get_circuit_dimensions():
    cables_1 = [['R3', 'U4', 'L2'], ['U2', 'R5']]
    assert get_circuit_dimensions(
        cables_1) == {'min_x': 0, 'max_x': 6, 'min_y': 0, 'max_y': 5}

    cables_2 = [['U4', 'R3', 'D2'], ['R5', 'U7']]
    assert get_circuit_dimensions(
        cables_2) == {'min_x': 0, 'max_x': 6, 'min_y': 0, 'max_y': 8}

# def test_get_distance_of_closest_intersection():

#     circuit_1 = """ \
# R3, U4, L2
# U2, R5
# """

#     """
#     ..--+..
#     ....|..
#     .+--x--
#     .|..|..
#     .0--+..
#     .......
#     """

#     assert get_distance_of_closest_intersection(circuit_1) == 5
