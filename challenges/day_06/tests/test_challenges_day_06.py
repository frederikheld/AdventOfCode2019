import pytest

from challenges.day_06.challenge_01 import day_06_challenge_01
# from challenges.day_06.challenge_02 import day_06_challenge_02


def test_actual_challenge_day_06_challenge_01():
    assert day_06_challenge_01() == 110190


# def test_actual_challenge_day_06_challenge_02():
#     assert day_06_challenge_02() == 'bar'  # valid solution of the challenge
