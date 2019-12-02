import os
from lib.calculate_fuel import calculate_total_fuel_from_list


def day01():
    f = open(
        os.path.dirname(os.path.realpath(__file__)) +
        '/data/input.txt', 'r'
    )
    return calculate_total_fuel_from_list(f.read())


if __name__ == "__main__":
    print(day01())
