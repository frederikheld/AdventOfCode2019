import pytest

from lib.universal_orbit_map.universal_orbit_map import UniversalOrbitMap

code1 = """ \
COM)B
B)A
"""

list1 = {
    'COM': ['B'],
    'B': ['A']
}

code2 = """ \
COM)B
B)A
COM)C
C)D
C)E
"""

list2 = {
    'COM': ['B', 'C'],
    'B': ['A'],
    'C': ['D', 'E']
}


def test_universal_orbit_map_init():
    uom = UniversalOrbitMap(code1, 'foo')
    assert isinstance(uom, UniversalOrbitMap)
    assert uom.getUniversalCenterOfMass() == 'foo'
    assert uom.getCode() == code1
    assert uom.getList() == list1


def test_universal_orbit_map_init_defaults():
    uom = UniversalOrbitMap(code1)
    assert uom.getUniversalCenterOfMass() == 'COM'


def test_universal_orbit_map_initlist():

    uom = UniversalOrbitMap(code2)
    orbits = uom.initList()

    assert orbits == list2


def test_universal_orbit_map_initorbits():
    uom = UniversalOrbitMap(code1, 'COM')

    orbits = uom.getOrbits()

    assert orbits.getName() == 'COM'
    assert orbits.getInOrbit()[0].getName() == 'B'
