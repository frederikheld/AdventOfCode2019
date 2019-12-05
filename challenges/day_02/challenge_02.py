import os

if __name__ == "__main__":
    from lib.intcode_solver import solve_intcode
else:
    from challenges.day_02.lib.intcode_solver import solve_intcode


def day_02_challenge_02():
    f = open(
        os.path.dirname(os.path.realpath(__file__)) +
        '/input/challenge_01_02.txt', 'r'
    )
    intcode = f.read()

    return solve_intcode(intcode, 19690720)


if __name__ == "__main__":
    print(day_02_challenge_02())
