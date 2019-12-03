import os

from ..lib.converter import intcode_to_list
from ..lib.converter import list_to_intcode
from ..lib.processor import process_intcode


def test_actual_challenge_day_01_challenge_01():
    f = open(
        os.path.dirname(os.path.realpath(__file__)) +
        '/../input/challenge_01.txt', 'r'
    )
    intcode_raw = f.read()
    intcode = intcode_to_list(intcode_raw)

    intcode[1] = '12'
    intcode[2] = '2'

    result_raw = process_intcode(list_to_intcode(intcode))
    result = intcode_to_list(result_raw)

    assert result[0] == '2842648'
