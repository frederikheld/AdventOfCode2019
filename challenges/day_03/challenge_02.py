import sys
import os

sys.path.append(os.path.join(os.path.dirname(
    os.path.dirname(sys.path[0]))))

try:
    from lib.circuit_solver.circuit_board import CircuitBoard
except:
    raise


def day_03_challenge_02():
    f = open(
        os.path.dirname(os.path.realpath(__file__)) +
        '/input/challenge_01_02.txt', 'r'
    )

    cb = CircuitBoard(f.read(), [1, 1])

    closest_to_start_intersection = cb.getClosestIntersectionAlongCables()

    return closest_to_start_intersection[1]


if __name__ == "__main__":
    print(day_03_challenge_02())
