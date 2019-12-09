import math


def calculate_fuel_from_mass(mass):
    """
    Fuel required to launch a given module is based on its mass.
    Specifically, to find the fuel required for a module,
    take its mass,
    divide by three,
    round down,
    and subtract 2.
    """

    return math.floor(mass / 3) - 2


def calculate_total_fuel_from_list(list, calculator=calculate_fuel_from_mass):
    """
    Calculate total fuel from a string that contains one mass specificaition per line.
    """
    total_fuel = 0
    for line in list.splitlines():
        total_fuel += calculator(int(line))

    return total_fuel
