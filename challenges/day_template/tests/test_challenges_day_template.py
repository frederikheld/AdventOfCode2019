import pytest

from challenges.day_template.challenge_01 import day_template_challenge_01
# from challenges.day_template.challenge_02 import day_template_challenge_02


def test_actual_challenge_day_template_challenge_01():
    assert day_template_challenge_01() == 'foo'  # valid solution of the challenge


# def test_actual_challenge_day_template_challenge_02():
#     assert day_template_challenge_02() == 'bar'  # valid solution of the challenge
