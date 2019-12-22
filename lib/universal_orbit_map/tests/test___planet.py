import pytest

from lib.universal_orbit_map.planet import Planet


def test_planet_init():
    planet = Planet('COM')
    assert isinstance(planet, Planet)
    assert planet.getName() == 'COM'
    assert planet.getCode() == None
    assert planet.getInOrbit() == []


def test_planet_putinorbit():
    COM = Planet('COM')
    A = Planet('A')
    COM.putInOrbit(A)

    assert COM.getInOrbit() == [A]

    B = Planet('B')
    COM.putInOrbit(B)

    assert COM.getInOrbit() == [A, B]


def test_planet_putinorbit_cascaded():
    """
            C
           /
    COM - A - B
    """
    COM = Planet('COM')
    A = Planet('A')
    B = Planet('B')
    C = Planet('C')

    COM.putInOrbit(A)
    A.putInOrbit(B)
    A.putInOrbit(C)

    assert COM.getInOrbit() == [A]
    assert A.getInOrbit() == [B, C]


def test_planet_gettotalnumberoforbits():
    """
            C
           /
    COM - A - B
    """
    COM1 = Planet('COM')
    A1 = Planet('A')
    B1 = Planet('B')
    C1 = Planet('C')

    COM1.putInOrbit(A1)
    A1.putInOrbit(B1)
    A1.putInOrbit(C1)

    assert COM1.getTotalNumberOfOrbits() == 5

    """
    COM - B - C - D
    """

    COM2 = Planet('COM')
    B2 = Planet('B')
    C2 = Planet('C')
    D2 = Planet('D')

    COM2.putInOrbit(B2)
    B2.putInOrbit(C2)
    C2.putInOrbit(D2)

    assert COM2.getTotalNumberOfOrbits() == 6

    """
    COM
    """

    COM3 = Planet('COM')

    assert COM3.getTotalNumberOfOrbits() == 0

    # """
    #         G - H       J - K - L
    #        /           /
    # COM - B - C - D - E - F
    #                \
    #                 I
    # """

    COM = Planet('COM')
    B = Planet('B')
    C = Planet('C')
    D = Planet('D')
    E = Planet('E')
    F = Planet('F')

    COM.putInOrbit(B)
    B.putInOrbit(C)
    C.putInOrbit(D)
    D.putInOrbit(E)
    E.putInOrbit(F)

    G = Planet('G')
    H = Planet('H')

    B.putInOrbit(G)
    G.putInOrbit(H)

    I = Planet('I')

    D.putInOrbit(I)

    J = Planet('J')
    K = Planet('K')
    L = Planet('L')

    E.putInOrbit(J)
    J.putInOrbit(K)
    K.putInOrbit(L)

    assert COM.getTotalNumberOfOrbits() == 42


def test_planet_initorbits():

    code = """ \
COM)ABC
COM)123
"""

    COM = Planet('COM', code)

    assert isinstance(COM.getInOrbit()[0], Planet)
    assert COM.getInOrbit()[0].getName() == 'ABC'
