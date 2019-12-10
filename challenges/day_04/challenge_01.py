import sys
import os

sys.path.append(os.path.join(os.path.dirname(
    os.path.dirname(sys.path[0]))))

try:
    from lib.password_solver.password_solver import password_solver
except:
    raise


def day_04_challenge_01():

    input = '147981-691423'

    range = input.split("-")

    matches = password_solver(int(range[0]), int(range[1]))

    return len(matches)


if __name__ == "__main__":
    print(day_04_challenge_01())
