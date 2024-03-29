import pytest

# import object under test:
from lib.circuit_solver.circuit_board import *
from lib.circuit_solver.cable import *

# import test fixtures:
from fixtures.circuit_board.circuit_1 import circuit_1
from fixtures.circuit_board.circuit_2 import circuit_2
from fixtures.circuit_board.circuit_3 import circuit_3
from fixtures.circuit_board.circuit_4 import circuit_4
from fixtures.circuit_board.circuit_5 import circuit_5
from fixtures.circuit_board.circuit_aoc_1 import circuit_aoc_1


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
    cf1_intersections = cf1.getIntersections()

    assert len(cf1_intersections) == 1
    assert cf1_intersections[0]['coordinates'] == circuit_1['intersections'][0]['coordinates']

    assert cf1_intersections[0]['cable_1'].getList() == cf1.getCables()[
        0].getList()
    assert cf1_intersections[0]['cable_2'].getList() == cf1.getCables()[
        1].getList()

    cf5 = CircuitBoard(circuit_5['raw'], circuit_5['start'])
    cf5_intersections = cf5.getIntersections()

    assert len(cf5_intersections) == 2
    assert cf5_intersections[0]['coordinates'] == circuit_5['intersections'][0]['coordinates']
    assert cf5_intersections[0]['cable_1'].getList() == cf5.getCables()[
        0].getList()
    assert cf5_intersections[0]['cable_2'].getList() == cf5.getCables()[
        1].getList()

    assert cf5_intersections[1]['coordinates'] == circuit_5['intersections'][1]['coordinates']
    assert cf5_intersections[1]['cable_1'].getList() == cf5.getCables()[
        1].getList()
    assert cf5_intersections[1]['cable_2'].getList() == cf5.getCables()[
        2].getList()


def test_get_closest_intersection():
    cf1 = CircuitBoard(circuit_1['raw'], circuit_1['start'])
    assert cf1.getClosestIntersection() == circuit_1['closest_intersection']

    cf2 = CircuitBoard(circuit_2['raw'], circuit_2['start'])
    assert cf2.getClosestIntersection() == circuit_2['closest_intersection']

    cfaoc1 = CircuitBoard(circuit_aoc_1['raw'], circuit_aoc_1['start'])
    assert cfaoc1.getClosestIntersection(
    ) == circuit_aoc_1['closest_intersection']


def test_get_closest_intersection_along_cables():
    cf1 = CircuitBoard(circuit_1['raw'], circuit_1['start'])
    assert cf1.getClosestIntersectionAlongCables(
    ) == circuit_1['closest_intersection_along_cables']

    cf4 = CircuitBoard(circuit_4['raw'], circuit_4['start'])
    assert cf4.getClosestIntersectionAlongCables(
    ) == circuit_4['closest_intersection_along_cables']

    cfaoc1 = CircuitBoard(circuit_aoc_1['raw'], circuit_aoc_1['start'])
    assert cfaoc1.getClosestIntersectionAlongCables(
    ) == circuit_aoc_1['closest_intersection_along_cables']

    cfaoc2_raw = """ \
R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83
"""
    cfaoc2 = CircuitBoard(cfaoc2_raw, [1, 1])
    assert cfaoc2.getClosestIntersectionAlongCables()[1] == 610

    cfaoc3_raw = """ \
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
"""
    cfaoc3 = CircuitBoard(cfaoc3_raw, [1, 1])
    assert cfaoc3.getClosestIntersectionAlongCables()[1] == 410
