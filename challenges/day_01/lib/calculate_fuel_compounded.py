from .calculate_fuel import calculate_fuel_from_mass


def calculate_fuel_from_mass_compounded(mass):
    """
    So, for each module mass,
    calculate its fuel and add it to the total.
    Then, treat the fuel amount you just calculated as the input mass and repeat the process,
    continuing until a fuel requirement is zero or negative.
    """

    add_fuel = calculate_fuel_from_mass(mass)
    fuel = add_fuel

    keep_going = True
    while keep_going:
        add_fuel = calculate_fuel_from_mass(add_fuel)
        if add_fuel > 0:
            fuel += add_fuel
        else:
            keep_going = False

    return fuel
