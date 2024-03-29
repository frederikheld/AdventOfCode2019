import pytest

from lib.intcode_computer.intcode_converter import intcode_to_list
from lib.intcode_computer.intcode_solver import solve_intcode
from lib.intcode_computer.intcode_processor import process_intcode


def test_intcode_solver():
    assert solve_intcode("1,9,10,3,2,3,11,0,99,30,40,50", 50) == 200
    assert solve_intcode("1,9,10,3,2,3,11,0,99,30,40,50", 5000) == 800
    assert solve_intcode("1,0,0,0,99", 1) == 200
    assert solve_intcode("1,0,0,0,99", 2) == 0
