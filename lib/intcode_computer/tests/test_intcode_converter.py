import pytest

from lib.intcode_computer.intcode_converter import *


def test_intcode_to_list():
    assert intcode_to_list("0, 0, 0") == [0, 0, 0]
    assert intcode_to_list("0, 0, 1") == [0, 0, 1]
    assert intcode_to_list("0,0,0") == [0, 0, 0]
    assert intcode_to_list("4 ,0,0") == [4, 0, 0]
    assert intcode_to_list("6") == [6]
    assert intcode_to_list("") == []

    list1 = """\
4 ,0,0,
5,8, 10, 0
"""
    assert intcode_to_list(list1) == [4, 0, 0, 5, 8, 10, 0]


def test_list_to_intcode():
    assert list_to_intcode(['0', '1', '5']) == "0,1,5"
    assert list_to_intcode(['10', '5', '8']) == "10,5,8"


def test_instruction_to_opcode_and_parameters():
    """
    ABCDE
     1002

    DE: two-digit opcode        02 -> 2
    C:  mode of 1st parameter    0 -> 0
    B:  mode of 2nd parameter    1 -> 1
    A:  mode of 3rd parameter      -> 0

    Parameter modes are optional and default to 0.
    """

    assert instruction_to_opcode_and_parameters(31002) == {
        'opcode': 2,
        'parameter_1': 0,
        'parameter_2': 1,
        'parameter_3': 3
    }

    assert instruction_to_opcode_and_parameters(1002) == {
        'opcode': 2,
        'parameter_1': 0,
        'parameter_2': 1,
        'parameter_3': 0
    }

    assert instruction_to_opcode_and_parameters(102) == {
        'opcode': 2,
        'parameter_1': 1,
        'parameter_2': 0,
        'parameter_3': 0
    }

    assert instruction_to_opcode_and_parameters('02') == {
        'opcode': 2,
        'parameter_1': 0,
        'parameter_2': 0,
        'parameter_3': 0
    }

    assert instruction_to_opcode_and_parameters('1') == {
        'opcode': 1,
        'parameter_1': 0,
        'parameter_2': 0,
        'parameter_3': 0
    }
