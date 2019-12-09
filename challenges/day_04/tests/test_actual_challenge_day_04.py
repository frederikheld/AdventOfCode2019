import pytest

from challenges.day_04.challenge_01 import day_04_challenge_01
from challenges.day_04.challenge_02 import day_04_challenge_02


def test_actual_challenge_day_04_challenge_01():
    assert day_04_challenge_01() == 1790


def test_actual_challenge_day_04_challenge_02():
    assert day_04_challenge_02() == 1206
