import operator

from .intcode_converter import intcode_to_list, instruction_to_opcode_and_parameters
from .intcode_converter import list_to_intcode


def process_intcode(intcode):

    intcode = intcode_to_list(intcode)

    instruction_pointer = 0

    while True:

        instruction = instruction_to_opcode_and_parameters(
            intcode[instruction_pointer])

        if instruction['opcode'] == 1:  # opcode 'add'
            operation = operator.add
            instruction_length = 4

        elif instruction['opcode'] == 2:  # opcode 'multiply'
            operation = operator.mul
            instruction_length = 4

        elif instruction['opcode'] == 99:  # opcode 'halt'
            return list_to_intcode(intcode)

        else:
            raise ValueError(
                str(instruction['opcode']) + ' is no valid opcode!')

        res = operation(
            intcode[intcode[instruction_pointer + 1]],
            intcode[intcode[instruction_pointer + 2]]
        )

        intcode[intcode[instruction_pointer + 3]] = res

        instruction_pointer += instruction_length
