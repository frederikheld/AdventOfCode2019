import pytest
import os

from challenges.day_01.challenge_01 import day_01_challenge_01
from challenges.day_01.challenge_02 import day_01_challenge_02


def test_actual_challenge_day_01_challenge_01():
    assert day_01_challenge_01() == 3315383


def test_actual_challenge_day_01_challenge_02():
    assert day_01_challenge_02() == 4970206
