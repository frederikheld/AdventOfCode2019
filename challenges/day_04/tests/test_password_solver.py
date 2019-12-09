import pytest

# import object under test:
from challenges.day_04.lib.password_solver import *


def test_password_solver():
    assert password_solver(111111, 111112) == [111111, 111112]
    assert password_solver(123444, 123460) == [
        123444, 123445, 123446, 123447, 123448, 123449, 123455]


def test_password_solver_no_large_groups():
    assert password_solver(123444, 123460, False) == [
        123445, 123446, 123447, 123448, 123449, 123455]

    assert password_solver(123488, 123566, False) == [
        123488, 123499, 123556, 123557, 123558, 123559, 123566]

    # print(password_solver(122888, 123360))
    # assert password_solver(122888, 123360, False) == [
    #     122888, 122889, 122899, 122999, 123344, 123345, 123346, 123347, 123348, 123349, 123355, 123356, 123357, 123358, 123359]


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

    assert check_two_adjacent_are_same(1) == False
    assert check_two_adjacent_are_same(11) == True

    assert check_two_adjacent_are_same(12325) == False


def test_check_two_adjacent_are_same_no_large_groups():
    assert check_two_adjacent_are_same(12344, False) == True
    assert check_two_adjacent_are_same(12234, False) == True
    assert check_two_adjacent_are_same(11234, False) == True

    assert check_two_adjacent_are_same(11222, False) == True
    assert check_two_adjacent_are_same(11122, False) == True
    assert check_two_adjacent_are_same(12233, False) == True

    assert check_two_adjacent_are_same(11111, False) == False

    assert check_two_adjacent_are_same(1, False) == False
    assert check_two_adjacent_are_same(11, False) == True
    assert check_two_adjacent_are_same(111, False) == False

    assert check_two_adjacent_are_same(112, False) == True
    assert check_two_adjacent_are_same(122, False) == True

    assert check_two_adjacent_are_same(12325, False) == False

    assert check_two_adjacent_are_same(123333, False) == False
    assert check_two_adjacent_are_same(123334, False) == False

    assert check_two_adjacent_are_same(1123456677, False) == True
    assert check_two_adjacent_are_same(111123456677, False) == True


def test_check_digits_never_decrease():
    assert check_digits_never_decrease(12345) == True
    assert check_digits_never_decrease(56789) == True
    assert check_digits_never_decrease(54321) == False
    assert check_digits_never_decrease(12325) == False
    assert check_digits_never_decrease(12331) == False
