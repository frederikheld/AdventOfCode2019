import pytest

# import object under test:
from challenges.day_03.lib.circuit_board import *
from challenges.day_03.lib.cable import *

# import test fixtures:
from challenges.day_03.tests.fixtures.circuit_board.circuit_1 import circuit_1
from challenges.day_03.tests.fixtures.circuit_board.circuit_2 import circuit_2
from challenges.day_03.tests.fixtures.circuit_board.circuit_3 import circuit_3
from challenges.day_03.tests.fixtures.circuit_board.circuit_4 import circuit_4
from challenges.day_03.tests.fixtures.circuit_board.circuit_aoc_1 import circuit_aoc_1


def test_object_instantiation():
    cf1 = CircuitBoard(circuit_1['raw'], circuit_1['start'])
    assert isinstance(cf1, CircuitBoard)
    assert cf1.getCode() == circuit_1['raw']
    assert cf1.getStart() == circuit_1['start']

    cf2 = CircuitBoard(circuit_2['raw'], circuit_2['start'])
    assert isinstance(cf2, CircuitBoard)
    assert cf2.getCode() == circuit_2['raw']
    assert cf2.getStart() == circuit_2['start']


def test_start_default():
    cf1 = CircuitBoard(circuit_1['raw'])
    assert cf1.getStart() == [1, 1]


def test_init_cables():
    cf1 = CircuitBoard(circuit_1['raw'], circuit_1['start'])
    cables1 = cf1.initCables()
    assert isinstance(cables1, list)
    assert len(cables1) == 2
    assert isinstance(cables1[0], Cable)
    assert isinstance(cables1[1], Cable)
    assert cables1[0].getStart() == circuit_1['start']

    cf2 = CircuitBoard(circuit_2['raw'], circuit_2['start'])
    cables2 = cf2.initCables()
    assert isinstance(cables2, list)
    assert len(cables2) == 2
    assert isinstance(cables2[0], Cable)
    assert isinstance(cables2[1], Cable)
    assert cables2[0].getStart() == circuit_2['start']

    cf3 = CircuitBoard(circuit_3['raw'])
    cables3 = cf3.initCables()
    assert isinstance(cables3, list)
    assert len(cables3) == 3


def test_get_intersections():
    cf1 = CircuitBoard(circuit_1['raw'], circuit_1['start'])
    assert cf1.getIntersections() == circuit_1['intersections']

    cf2 = CircuitBoard(circuit_2['raw'], circuit_2['start'])
    assert cf2.getIntersections() == circuit_2['intersections']


def test_get_closest_intersection():
    cf1 = CircuitBoard(circuit_1['raw'], circuit_1['start'])
    assert cf1.getClosestIntersection() == circuit_1['closest_intersection']

    cf2 = CircuitBoard(circuit_2['raw'], circuit_2['start'])
    assert cf2.getClosestIntersection() == circuit_2['closest_intersection']

    cfaoc1 = CircuitBoard(circuit_aoc_1['raw'], circuit_aoc_1['start'])
    assert cfaoc1.getClosestIntersection(
    ) == circuit_aoc_1['closest_intersection']


# def test_get_closest_intersection_along_cables():
#     cf1 = CircuitBoard(circuit_1['raw'], circuit_1['start'])
#     assert cf1.getClosestIntersectionAlongCables(
#     ) == circuit_1['closest_intersection_along_cables']

    # cf4 = CircuitBoard(circuit_4['raw'], circuit_4['start'])
    # assert cf4.getClosestIntersectionAlongCables(
    # ) == circuit_4['closest_intersection_along_cables']

    # cfaoc1 = CircuitBoard(circuit_aoc_1['raw'], circuit_aoc_1['start'])
    # assert cfaoc1.getClosestIntersectionAlongCables(
    # ) == circuit_aoc_1['closest_intersection_along_cables']
