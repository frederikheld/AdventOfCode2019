import pytest

# import object under test:
from challenges.day_04.lib.password_solver import *


def test_password_solver():
    assert password_solver(111111, 111112) == [111111, 111112]
    assert password_solver(123444, 123460) == [
        123444, 123445, 123446, 123447, 123448, 123449, 123455]


def test_check_six_digits():
    assert check_six_digits(123456) == True
    assert check_six_digits(12345) == False
    assert check_six_digits(1234567) == False


def test_check_within_range():
    assert check_within_range([1, 5], 2) == True

    assert check_within_range([2, 5], 2) == True
    assert check_within_range([3, 5], 2) == False

    assert check_within_range([2, 5], 5) == True
    assert check_within_range([2, 4], 5) == False


def test_check_two_adjacent_are_same():
    assert check_two_adjacent_are_same(12345) == False
    assert check_two_adjacent_are_same(11245) == True
    assert check_two_adjacent_are_same(12245) == True
    assert check_two_adjacent_are_same(12225) == True
    assert check_two_adjacent_are_same(12344) == True
    assert check_two_adjacent_are_same(11111) == True

    assert check_two_adjacent_are_same(11) == True
    assert check_two_adjacent_are_same(1) == False

    assert check_two_adjacent_are_same(12325) == False


def test_check_digits_never_decrease():
    assert check_digits_never_decrease(12345) == True
    assert check_digits_never_decrease(56789) == True
    assert check_digits_never_decrease(54321) == False
    assert check_digits_never_decrease(12325) == False
    assert check_digits_never_decrease(12331) == False
