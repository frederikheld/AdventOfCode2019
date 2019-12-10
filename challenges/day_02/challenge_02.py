import sys
import os

sys.path.append(os.path.join(os.path.dirname(
    os.path.dirname(sys.path[0]))))

try:
    from lib.intcode_computer.intcode_solver import solve_intcode
except:
    raise


def day_02_challenge_02():
    f = open(
        os.path.dirname(os.path.realpath(__file__)) +
        '/input/challenge_01_02.txt', 'r'
    )
    intcode = f.read()

    return solve_intcode(intcode, 19690720)


if __name__ == "__main__":
    print(day_02_challenge_02())
