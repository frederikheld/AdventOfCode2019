import operator

from .intcode_converter import intcode_to_list
from .intcode_converter import list_to_intcode
from .intcode_processor import process_intcode


def solve_intcode(intcode, expected_output):

    intcode = intcode_to_list(intcode)

    for verb in range(0, 100):
        for noun in range(0, 100):

            memory = intcode

            memory[1] = noun
            memory[2] = verb

            output = process_intcode(list_to_intcode(memory))

            if intcode_to_list(output)[0] == expected_output:
                return 100 * noun + verb

    return None
