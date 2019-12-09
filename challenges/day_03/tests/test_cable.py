import pytest

# import object under test:
from challenges.day_03.lib.cable import *

# import test fixtures:
from challenges.day_03.tests.fixtures.circuit_board.cable_1 import *
from challenges.day_03.tests.fixtures.circuit_board.cable_2 import *
from challenges.day_03.tests.fixtures.circuit_board.cable_3 import *


def test_object_instantiation():
    cf1 = Cable(cable_1['code'], cable_1['start'])
    assert isinstance(cf1, Cable)
    assert cf1.getCode() == cable_1['code']
    assert cf1.getList() == cable_1['list']
    assert cf1.getStart() == cable_1['start']
    assert cf1.getSections() == cable_1['sections']

    cf2 = Cable(cable_2['code'], cable_2['start'])
    assert isinstance(cf2, Cable)
    assert cf2.getCode() == cable_2['code']
    assert cf2.getStart() == cable_2['start']


def test_start_default():
    cf1 = Cable(cable_1['code'])
    assert cf1.getStart() == [0, 0]


def test_init_list():
    cf1 = Cable(cable_1['code'])
    assert cf1.initList() == cable_1['list']

    cf2 = Cable(cable_2['code'])
    assert cf2.initList() == cable_2['list']


def test_init_sections():
    cf1 = Cable(cable_1['code'], cable_1['start'])
    assert cf1.initSections() == cable_1['sections']

    cf2 = Cable(cable_2['code'], cable_2['start'])
    assert cf2.initSections() == cable_2['sections']


def test_intersect():
    cf1_1 = Cable(cable_1['code'], cable_1['start'])
    cf1_2 = Cable(cable_1_1['code'], cable_1_1['start'])
    assert cf1_1.intersect(cf1_2) == cable_1['intersections']

    # cf2_1 = Cable(cable_2['code'], cable_2['start'])
    # cf2_2 = Cable(cable_2_1['code'], cable_2_1['start'])
    # assert cf2_1.intersect(cf2_2) == cable_2['intersections']


def test_get_distance_along_cable():
    cf1 = Cable(cable_1['code'], cable_1['start'])
    assert cf1.getDistanceAlongCable(
        cable_1['intersections'][0]) == cable_1['distance_along_cable'][0]  # distance = 0
    assert cf1.getDistanceAlongCable(
        cable_1['intersections'][1]) == cable_1['distance_along_cable'][1]  # distance = 4

    cf2 = Cable(cable_2['code'], cable_2['start'])
    assert cf2.getDistanceAlongCable(
        cable_2['intersections'][0]) == cable_2['distance_along_cable'][0]  # distance = 1

    cf3 = Cable(cable_3['code'], cable_3['start'])
    assert cf3.getDistanceAlongCable(
        cable_3['intersections'][1]) == cable_3['distance_along_cable'][1]  # distance = 17

    assert cf3.getDistanceAlongCable([10, 100]) == None  # point not on cable
