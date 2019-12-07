import pytest

# import object under test:
from challenges.day_03.lib.circuit_board import *

# import test fixtures:
from challenges.day_03.tests.fixtures.circuit_board.circuit_1 import circuit_1
from challenges.day_03.tests.fixtures.circuit_board.circuit_2 import circuit_2
from challenges.day_03.tests.fixtures.circuit_board.circuit_aoc_1 import circuit_aoc_1


def test_object_instantiation():
    cf1 = CircuitBoard(circuit_1['raw'])
    assert isinstance(cf1, CircuitBoard)
    assert cf1.getCircuit() == circuit_1['raw']
    assert cf1.getCables() == circuit_1['cables']

    cf2 = CircuitBoard(circuit_2['raw'])
    assert isinstance(cf2, CircuitBoard)
    assert cf2.getCircuit() == circuit_2['raw']
    assert cf2.getCables() == circuit_2['cables']


def test_init_cables():
    cf1 = CircuitBoard(circuit_1['raw'])
    assert cf1.initCables() == circuit_1['cables']

    cf2 = CircuitBoard(circuit_2['raw'])
    assert cf2.initCables() == circuit_2['cables']
