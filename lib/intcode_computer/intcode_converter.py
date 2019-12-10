def intcode_to_list(intcode):
    if intcode == "":
        return []

    return [int(x) for x in intcode.replace(" ", "").replace("\n", "").split(",")]


def list_to_intcode(lst):
    return ",".join(str(x) for x in lst)


def instruction_to_opcode_and_parameters(instruction):
    opcode = int(str(instruction)[-2:])
    parameter_1 = int(str(instruction)[-3:-2] or 0)
    parameter_2 = int(str(instruction)[-4:-3] or 0)
    parameter_3 = int(str(instruction)[-5:-4] or 0)
    result = {
        'opcode': opcode,
        'parameter_1': parameter_1,
        'parameter_2': parameter_2,
        'parameter_3': parameter_3
    }

    return result
