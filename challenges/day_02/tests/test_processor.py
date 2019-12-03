import pytest

from ..lib.processor import *


def test_process_add():
    intcode1 = """\
1,9,10,3,
2,3,11,0,
99,
30,40,50
"""
    result1 = "1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50"

    assert process_intcode(intcode1) == result1

    intcode2 = """\
1,9,10,4,
2,3,11,0,
99,
30,50,50
"""
    result2 = "1, 9, 10, 4, 80, 3, 11, 0, 99, 30, 50, 50"

    assert process_intcode(intcode2) == result2


def test_process_multiply():
    intcode1 = "2, 2, 5, 4, 10, 8, 17, 1, 28, 12"
    result1 = "2, 2, 5, 4, 40, 8, 17, 1, 28, 12"

    assert process_intcode(intcode1) == result1

    intcode2 = "2, 2, 3, 4, 10, 8, 17, 1, 28, 12"
    result2 = "2, 2, 3, 4, 12, 8, 17, 1, 28, 12"

    assert process_intcode(intcode2) == result2
