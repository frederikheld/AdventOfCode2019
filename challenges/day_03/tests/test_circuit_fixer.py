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


def test_get_intersections():
    cf1 = CircuitFixer(circuit_1['raw'])
    assert cf1.getIntersections() == circuit_1['intersections']

    cf2 = CircuitFixer(circuit_2['raw'])
    assert cf2.getIntersections() == circuit_2['intersections']


def test_get_closest_intersection():
    cf1 = CircuitFixer(circuit_1['raw'])
    assert cf1.getClosestIntersection() == circuit_1['closest_intersection']

    cf2 = CircuitFixer(circuit_2['raw'])
    assert cf2.getClosestIntersection() == circuit_2['closest_intersection']
