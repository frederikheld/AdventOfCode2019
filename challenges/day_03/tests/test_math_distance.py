import pytest

from challenges.day_03.lib.math_distance import *


def test_calculate_manhattan_distance():
    """
    .....e
    ......
    s.....
    """
    assert calculate_manhattan_distance(
        [0, 0],
        [5, 2]
    ) == 7

    """
    .....e
    ...s..
    ......
    """
    assert calculate_manhattan_distance(
        [3, 1],
        [5, 2]
    ) == 3

    """
    .e....
    ......
    ...s..
    """
    assert calculate_manhattan_distance(
        [3, 0],
        [1, 2]
    ) == 4

    """
    .s....
    ......
    ....e.
    """
    assert calculate_manhattan_distance(
        [1, 2],
        [4, 0]
    ) == 5
    """
    ....s.
    ..e...
    ......
    """
    assert calculate_manhattan_distance(
        [4, 2],
        [2, 1]
    ) == 3
