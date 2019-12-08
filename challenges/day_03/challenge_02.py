import os

if __name__ == "__main__":
    from lib.circuit_board import CircuitBoard
else:
    from challenges.day_03.lib.circuit_board import CircuitBoard


def day_03_challenge_02():
    f = open(
        os.path.dirname(os.path.realpath(__file__)) +
        '/input/challenge_01.txt', 'r'
    )

    cb = CircuitBoard(f.read(), [1, 1])

    closest_to_start_intersection = cb.getClosestToStartIntersection()

    return closest_to_start_intersection[1]


if __name__ == "__main__":
    print(day_03_challenge_02())
