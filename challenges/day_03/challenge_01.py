import os

if __name__ == "__main__":
    from lib.circuit_fixer import CircuitFixer
else:
    from challenges.day_03.lib.circuit_fixer import CircuitFixer


def day_03_challenge_01():
    f = open(
        os.path.dirname(os.path.realpath(__file__)) +
        '/input/challenge_01.txt', 'r'
    )

    circuit = f.read()

    circuit_fixer = CircuitFixer(circuit)

    closest_intersection = circuit_fixer.getClosestIntersection()

    return closest_intersection[1]


if __name__ == "__main__":
    print(day_03_challenge_01())
