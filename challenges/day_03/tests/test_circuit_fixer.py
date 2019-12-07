import pytest

# import object under test:
from challenges.day_03.lib.circuit_fixer import *

# import test fixtures:
from challenges.day_03.tests.fixtures.circuit_fixer.circuit_1 import circuit_1
from challenges.day_03.tests.fixtures.circuit_fixer.circuit_2 import circuit_2


def test_object_instantiation():
    cf1 = CircuitFixer(circuit_1['raw'])
    assert isinstance(cf1, CircuitFixer)
    assert cf1.getCircuit() == circuit_1['raw']
    assert cf1.getCables() == circuit_1['cables']

    cf2 = CircuitFixer(circuit_2['raw'])
    assert isinstance(cf2, CircuitFixer)
    assert cf2.getCircuit() == circuit_2['raw']
    assert cf2.getCables() == circuit_2['cables']


def test_init_cables():
    cf1 = CircuitFixer(circuit_1['raw'])
    assert cf1.initCables() == circuit_1['cables']

    cf2 = CircuitFixer(circuit_2['raw'])
    assert cf2.initCables() == circuit_2['cables']


def test_get_circuit_dimensions():
    cf1 = CircuitFixer(circuit_1['raw'])
    assert cf1.initCircuitDimensions() == circuit_1['dimensions']

    cf2 = CircuitFixer(circuit_2['raw'])
    assert cf2.initCircuitDimensions() == circuit_2['dimensions']


def test_get_occupancy_map():
    # cf1 = CircuitFixer(circuit_1['raw'])
    # assert cf1.getOccupancyMap() == circuit_1['occupancy_map']

    cf2 = CircuitFixer(circuit_2['raw'])
    assert cf2.getOccupancyMap() == circuit_2['occupancy_map']

# def test_get_distance_of_closest_intersection():

    #     circuit_1 = """ \
    # R3, U2
    # U1, R5
    # """

    #     """
    #     ....|..
    #     .+--x--
    #     .0--+..
    #     .......
    #     """

    #     assert get_distance_of_closest_intersection(circuit_1) == 4

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

    # def test_get_intersections():
    #     circuit_1 = [
    #         [0, 0, 0], [0, 2, 1], [0, 1, 1],
    #         [0, 1, 1], [0, 1, 2], [0, 0, 1]
    #     ]
    #     assert(get_intersections(circuit_1)) == [[1, 1], [4, 2]]

    #     circuit_2 = [[0, 0, 2, 2], [0, 2, 0, 0], [0, 1, 1, 0]]
    #     assert(get_intersections(circuit_2)) == [[0, 2], [0, 3], [1, 1]]

    # def test_get_circuit_dimensions():
    #     cables_1 = [['R3', 'U4', 'L2'], ['U2', 'R5']]
    #     assert get_circuit_dimensions(
    #         cables_1) == {'min_x': 0, 'max_x': 6, 'min_y': 0, 'max_y': 5}

    #     cables_2 = [['U4', 'R3', 'D2'], ['R5', 'U7']]
    #     assert get_circuit_dimensions(
    #         cables_2) == {'min_x': 0, 'max_x': 6, 'min_y': 0, 'max_y': 8}

    #     cables_3 = [['R3', 'U2'], ['U1', 'R5']]
    #     assert get_circuit_dimensions(
    #         cables_3) == {'min_x': 0, 'max_x': 6, 'min_y': 0, 'max_y': 3}
