import pytest

from ..lib.converter import *


def test_intcode_to_list():
    assert intcode_to_list("0, 0, 0") == ['0', '0', '0']
    assert intcode_to_list("0, 0, 1") == ['0', '0', '1']
    assert intcode_to_list("0,0,0") == ['0', '0', '0']
    assert intcode_to_list("4 ,0,0") == ['4', '0', '0']
    assert intcode_to_list("6") == ['6']
    assert intcode_to_list("") == []

    list1 = """\
4 ,0,0,
5,8, 10, 0
"""
    assert intcode_to_list(list1) == ['4', '0', '0', '5', '8', '10', '0']


def test_list_to_intcode():
    assert list_to_intcode(['0', '1', '5']) == "0,1,5"
    assert list_to_intcode(['10', '5', '8']) == "10,5,8"
