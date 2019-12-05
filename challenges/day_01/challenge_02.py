import os

if __name__ == "__main__":
    from lib.calculate_fuel import calculate_total_fuel_from_list
    from lib.calculate_fuel_compounded import calculate_fuel_from_mass_compounded
else:
    from challenges.day_01.lib.calculate_fuel import calculate_total_fuel_from_list
    from challenges.day_01.lib.calculate_fuel_compounded import calculate_fuel_from_mass_compounded


def day_01_challenge_02():
    f = open(
        os.path.dirname(os.path.realpath(__file__)) +
        '/input/challenge_02.txt', 'r'
    )
    return calculate_total_fuel_from_list(f.read(), calculate_fuel_from_mass_compounded)


if __name__ == "__main__":
    print(day_01_challenge_02())
