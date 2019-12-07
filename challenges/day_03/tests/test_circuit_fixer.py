import pytest

# import object under test:
from challenges.day_03.lib.circuit_fixer import *

# import test fixtures:
from challenges.day_03.tests.fixtures.circuit_fixer.circuit_1 import circuit_1
from challenges.day_03.tests.fixtures.circuit_fixer.circuit_2 import circuit_2
from challenges.day_03.tests.fixtures.circuit_fixer.circuit_aoc_1 import circuit_aoc_1


def test_object_instantiation():
    cf1 = CircuitFixer(circuit_1['raw'])
    assert isinstance(cf1, CircuitFixer)
    assert cf1.getCircuit() == circuit_1['raw']
    assert cf1.getCables() == circuit_1['cables']
    assert cf1.getDimensions() == circuit_1['dimensions']
    assert cf1.getOccupancyMap() == circuit_1['occupancy_map']

    cf2 = CircuitFixer(circuit_2['raw'])
    assert isinstance(cf2, CircuitFixer)
    assert cf2.getCircuit() == circuit_2['raw']
    assert cf2.getCables() == circuit_2['cables']
    assert cf2.getDimensions() == circuit_2['dimensions']
    assert cf2.getOccupancyMap() == circuit_2['occupancy_map']


def test_init_cables():
    cf1 = CircuitFixer(circuit_1['raw'])
    assert cf1.initCables() == circuit_1['cables']

    cf2 = CircuitFixer(circuit_2['raw'])
    assert cf2.initCables() == circuit_2['cables']


def test_init_dimensions():
    cf1 = CircuitFixer(circuit_1['raw'])
    assert cf1.initDimensions() == circuit_1['dimensions']

    cf2 = CircuitFixer(circuit_2['raw'])
    assert cf2.initDimensions() == circuit_2['dimensions']


def test_init_occupancy_map():
    cf1 = CircuitFixer(circuit_1['raw'])
    assert cf1.initOccupancyMap() == circuit_1['occupancy_map']

    cf2 = CircuitFixer(circuit_2['raw'])
    assert cf2.initOccupancyMap() == circuit_2['occupancy_map']

    cfaoc1 = CircuitFixer(circuit_aoc_1['raw'])
    assert cfaoc1.initOccupancyMap() == circuit_aoc_1['occupancy_map']


def test_get_intersections():
    cf1 = CircuitFixer(circuit_1['raw'])
    assert cf1.getIntersections() == circuit_1['intersections']

    cf2 = CircuitFixer(circuit_2['raw'])
    assert cf2.getIntersections() == circuit_2['intersections']

    cfaoc1 = CircuitFixer(circuit_aoc_1['raw'])
    assert cfaoc1.getIntersections() == circuit_aoc_1['intersections']


def test_get_closest_intersection():
    cf1 = CircuitFixer(circuit_1['raw'])
    assert cf1.getClosestIntersection() == circuit_1['closest_intersection']

    cf2 = CircuitFixer(circuit_2['raw'])
    assert cf2.getClosestIntersection() == circuit_2['closest_intersection']

    cfaoc1 = CircuitFixer(circuit_aoc_1['raw'])
    assert cfaoc1.getClosestIntersection(
    ) == circuit_aoc_1['closest_intersection']

    # more examples from the website:
    cfaoc2 = CircuitFixer(""" \
R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83
""")
    cfaoc2_closest_intersection = cfaoc2.getClosestIntersection()

    # om = cfaoc2.getOccupancyMap()
    # for line in om:
    #     print(line)
    # print('--')

    print(cfaoc2.getIntersections())
    print(cfaoc2_closest_intersection)

    # assert cfaoc2_closest_intersection[1] == 159

    cfaoc3 = CircuitFixer(""" \
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
""")
    cfaoc3_closest_intersection = cfaoc3.getClosestIntersection()

    # print('--')
    # om = cfaoc3.getOccupancyMap()
    # for line in om:
    #     print(line)
    # print('--')

    print('--')
    cf1 = CircuitFixer(circuit_1['raw'])
    om = cf1.getOccupancyMap()
    for line in om:
        print(line)
    print('--')

    assert False
    # assert cfaoc3_closest_intersection[1] == 135
