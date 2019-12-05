import operator

from .intcode_converter import intcode_to_list
from .intcode_converter import list_to_intcode
from .intcode_processor import process_intcode


def solve_intcode(intcode, expected_output):

    intcode = intcode_to_list(intcode)

    for noun in range(0, 100):
        for verb in range(0, 100):
            current_intcode = intcode
            current_intcode[1] = noun
            current_intcode[2] = verb
            current_intcode = list_to_intcode(intcode)

            # print(current_intcode)
            output = process_intcode(current_intcode)

            if output == expected_output:
                return 100 * noun + verb

    return None
