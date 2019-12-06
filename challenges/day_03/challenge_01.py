import os

if __name__ == "__main__":
    from lib.fix_circuit import get_distance_of_closest_intersection
else:
    from challenges.day_03.lib.fix_circuit import get_distance_of_closest_intersection


def day_03_challenge_01():
    f = open(
        os.path.dirname(os.path.realpath(__file__)) +
        '/input/challenge_01.txt', 'r'
    )

    return get_distance_of_closest_intersection(f.read())


if __name__ == "__main__":
    print(day_03_challenge_01())
