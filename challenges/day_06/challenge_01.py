import sys
import os

sys.path.append(os.path.join(os.path.dirname(
    os.path.dirname(sys.path[0]))))

try:
    from lib.universal_orbit_map.planet import Planet
except:
    raise


def day_06_challenge_01():
    f = open(
        os.path.dirname(os.path.realpath(__file__)) +
        '/input/challenge_01.txt', 'r'
    )

    planet = Planet('COM')
    planet.initOrbitsFromCode(f.read())

    result = planet.getTotalNumberOfOrbits()

    return result


if __name__ == "__main__":
    print(day_06_challenge_01())

# don't forget to add it to main.py as well!
