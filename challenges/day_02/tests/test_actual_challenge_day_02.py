import os

from challenges.day_02.challenge_01 import day_02_challenge_01
from challenges.day_02.challenge_02 import day_02_challenge_02


def test_actual_challenge_day_01_challenge_01():
    assert day_02_challenge_01() == 2842648


def test_actual_challenge_day_01_challenge_02():
    assert day_02_challenge_02() == [12, 5, 6, 17]
