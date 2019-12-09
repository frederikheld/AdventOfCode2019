import operator

from .intcode_converter import intcode_to_list
from .intcode_converter import list_to_intcode


def process_intcode(intcode):

    intcode = intcode_to_list(intcode)

    instruction_pointer = 0

    while True:

        if intcode[instruction_pointer] == 1:  # opcode 'add'
            operation = operator.add
            instruction_length = 4

        elif intcode[instruction_pointer] == 2:  # opcode 'multiply'
            operation = operator.mul
            instruction_length = 4

        elif intcode[instruction_pointer] == 99:  # opcode 'halt'
            return list_to_intcode(intcode)

        res = operation(
            intcode[intcode[instruction_pointer + 1]],
            intcode[intcode[instruction_pointer + 2]]
        )

        intcode[intcode[instruction_pointer + 3]] = res

        instruction_pointer += instruction_length
