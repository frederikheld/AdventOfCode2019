import pytest

from challenges.day_02.lib.intcode_processor import process_intcode


def test_intcode_processor():
    assert process_intcode(
        "1,9,10,3,2,3,11,0,99,30,40,50") == "3500,9,10,70,2,3,11,0,99,30,40,50"
    assert process_intcode("1,0,0,0,99") == "2,0,0,0,99"
    assert process_intcode("2,3,0,3,99") == "2,3,0,6,99"
    assert process_intcode("2,4,4,5,99,0") == "2,4,4,5,99,9801"
    assert process_intcode("1,1,1,4,99,5,6,0,99") == "30,1,1,4,2,5,6,0,99"
