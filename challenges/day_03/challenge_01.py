import os

if __name__ == "__main__":
    from lib.circuit_board import CircuitBoard
else:
    from challenges.day_03.lib.circuit_board import CircuitBoard


def day_03_challenge_01():
    f = open(
        os.path.dirname(os.path.realpath(__file__)) +
        '/input/challenge_01.txt', 'r'
    )

    circuit = f.read()

    # TODO

    return 'foo'


if __name__ == "__main__":
    print(day_03_challenge_01())
