import pytest

# import object under test:
from challenges.day_03.lib.math_geometry import *


def test_intersect_two_lines():

    # example 1:
    """
    ..|...
    .-x---
    ..|...
    ......
    """
    line_1_1 = [
        [2, 1],
        [2, 3]
    ]
    line_1_2 = [
        [1, 2],
        [5, 2]
    ]
    intersection_1 = [2, 2]

    assert intersect(line_1_1, line_1_2) == intersection_1

    # example 2:

    """
    ....|.
    ....|.
    ----X-
    """
    line_2_1 = [
        [0, 0],
        [5, 0]
    ]
    line_2_2 = [
        [4, 0],
        [4, 2]
    ]
    intersection_2 = [4, 0]

    assert intersect(line_2_1, line_2_2) == intersection_2
