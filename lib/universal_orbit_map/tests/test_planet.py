import pytest

from lib.universal_orbit_map.planet import Planet


def test_planet_init():
    planet = Planet('foo')

    assert planet.getName() == 'foo'
    assert planet.getCode() == None
    assert planet.getPlanetsInOwnOrbit() == []
    assert planet.getInOrbitOf() == None

    planet2 = Planet('bar', 'ABC)DEF')

    assert planet2.getCode() == 'ABC)DEF'
    assert planet2.getName() == 'bar'
    assert planet2.getPlanetsInOwnOrbit() == []
    assert planet2.getInOrbitOf() == None


def test_putinorbitof():
    """
    Planet can put itself in orbit of one other planet
    """
    planet = Planet('planet')

    the_other_planet = Planet('the other planet')
    planet.putInOrbitOf(the_other_planet)

    assert planet.getInOrbitOf() == the_other_planet

    another_planet = Planet('another planet')
    planet.putInOrbitOf(another_planet)

    assert planet.getInOrbitOf() == another_planet


def test_putinownorbit():
    """
    Planet can put multiple planets in its own orbit
    """

    planet = Planet('planet')
    planet2 = Planet('planet 2')
    planet3 = Planet('planet 3')
    planet4 = Planet('planet 4')

    assert planet.getPlanetsInOwnOrbit() == []

    planet.putInOwnOrbit(planet2)
    assert planet.getPlanetsInOwnOrbit() == [planet2]

    planet.putInOwnOrbit(planet3)
    assert planet.getPlanetsInOwnOrbit() == [planet2, planet3]

    planet.putInOwnOrbit(planet4)
    assert planet.getPlanetsInOwnOrbit() == [planet2, planet3, planet4]


def test_putinorbitof_linksinbothdirections():
    """
    If Planet B is put in orbit of Planet A, Planet A will be put as
    isInOrbitOf of Planet B.
    """

    planetA = Planet('A')
    planetB = Planet('B')

    assert planetA.getPlanetsInOwnOrbit() == []
    assert planetB.getInOrbitOf() == None

    planetA.putInOwnOrbit(planetB)

    assert planetA.getPlanetsInOwnOrbit() == [planetB]
    assert planetB.getInOrbitOf() == planetA


def test_putinownorbit_linksinbothdirections():
    """
    If Planet B is set as putInOrbitOf() of Planet A,
    Planet A will putInOwnOrbit() Planet B.
    """

    planetA = Planet('A')
    planetB = Planet('B')

    assert planetA.getPlanetsInOwnOrbit() == []
    assert planetB.getInOrbitOf() == None

    planetB.putInOrbitOf(planetA)

    assert planetA.getPlanetsInOwnOrbit() == [planetB]
    assert planetB.getInOrbitOf() == planetA


def test_convertcodetodict():

    code = """ \
ABC)DEF
DEF)GHI
ABC)123
"""

    expected_result = {
        'ABC': ['DEF', '123'],
        'DEF': ['GHI']
    }

    planet = Planet('ABC', code)
    result = planet.convertCodeToDict()

    assert result == expected_result


def test_initorbitsfromcode():

    code = """ \
ABC)DEF
DEF)GHI
ABC)123
"""

    planet = Planet('ABC', code)

    # assert planet.getPlanetsInOwnOrbit()[0].getName() == 'DEF'
    # assert planet.getPlanetsInOwnOrbit()[1].getName() == '123'

    # assert planet.getPlanetsInOwnOrbit()[1].getPlanetsInOwnOrbit()[
    #     0].getName() == 'GHI'
