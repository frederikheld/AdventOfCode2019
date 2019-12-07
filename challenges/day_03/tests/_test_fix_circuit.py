import pytest

from challenges.day_03.lib.fix_circuit import *


def test_get_distance_of_closest_intersection():

    circuit_1 = """ \
R3, U2
U1, R5
"""

    """
    ....|..
    .+--x--
    .0--+..
    .......
    """

    assert get_distance_of_closest_intersection(circuit_1) == 4

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


def test_get_intersections():
    circuit_1 = [
        [0, 0, 0], [0, 2, 1], [0, 1, 1],
        [0, 1, 1], [0, 1, 2], [0, 0, 1]
    ]
    assert(get_intersections(circuit_1)) == [[1, 1], [4, 2]]

    circuit_2 = [[0, 0, 2, 2], [0, 2, 0, 0], [0, 1, 1, 0]]
    assert(get_intersections(circuit_2)) == [[0, 2], [0, 3], [1, 1]]


def test_get_circuit_dimensions():
    cables_1 = [['R3', 'U4', 'L2'], ['U2', 'R5']]
    assert get_circuit_dimensions(
        cables_1) == {'min_x': 0, 'max_x': 6, 'min_y': 0, 'max_y': 5}

    cables_2 = [['U4', 'R3', 'D2'], ['R5', 'U7']]
    assert get_circuit_dimensions(
        cables_2) == {'min_x': 0, 'max_x': 6, 'min_y': 0, 'max_y': 8}

    cables_3 = [['R3', 'U2'], ['U1', 'R5']]
    assert get_circuit_dimensions(
        cables_3) == {'min_x': 0, 'max_x': 6, 'min_y': 0, 'max_y': 3}
