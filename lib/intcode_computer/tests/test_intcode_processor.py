import pytest

from lib.intcode_computer.intcode_processor import process_intcode


def test_intcode_processor_unknown_opcode():
    with pytest.raises(ValueError):
        process_intcode("12,3,0,3,99")


def test_intcode_processor_add():
    assert process_intcode(
        "1,9,10,3,2,3,11,0,99,30,40,50") == "3500,9,10,70,2,3,11,0,99,30,40,50"
    assert process_intcode("1,0,0,0,99") == "2,0,0,0,99"
    assert process_intcode("1,1,1,4,99,5,6,0,99") == "30,1,1,4,2,5,6,0,99"

    # assert process_intcode("1001,0,0,0,99") == "2,0,0,0,99"


def test_intcode_processor_multiply():
    assert process_intcode("2,3,0,3,99") == "2,3,0,6,99"
    assert process_intcode("2,4,4,5,99,0") == "2,4,4,5,99,9801"


# def test_intcode_processor_input():
#     assert process_intcode("3,50") == None


# def test_intcode_processor_parameter_mode():
#     None
