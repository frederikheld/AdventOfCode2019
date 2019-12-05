import os

if __name__ == "__main__":
    from lib.intcode_converter import intcode_to_list
    from lib.intcode_converter import list_to_intcode
    from lib.intcode_processor import process_intcode
else:
    from challenges.day_02.lib.intcode_converter import intcode_to_list
    from challenges.day_02.lib.intcode_converter import list_to_intcode
    from challenges.day_02.lib.intcode_processor import process_intcode


def day_02_challenge_01():
    f = open(
        os.path.dirname(os.path.realpath(__file__)) +
        '/input/challenge_01_02.txt', 'r'
    )
    intcode_raw = f.read()
    intcode = intcode_to_list(intcode_raw)

    intcode[1] = 12
    intcode[2] = 2

    result_raw = process_intcode(list_to_intcode(intcode))
    result = intcode_to_list(result_raw)

    return result[0]


if __name__ == "__main__":
    print(day_02_challenge_01())
