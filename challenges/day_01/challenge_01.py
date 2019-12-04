import os

from challenges.day_01.lib.calculate_fuel import calculate_total_fuel_from_list


def day_01_challenge_01():
    f = open(
        os.path.dirname(os.path.realpath(__file__)) +
        '/input/challenge_01.txt', 'r'
    )
    return calculate_total_fuel_from_list(f.read())


if __name__ == "__main__":
    print(day_01_challenge_01())
