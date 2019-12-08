import pytest

# import object under test:
from challenges.day_03.lib.math_geometry import *


def test_intersect_two_lines():

    # example 1: intersection in the middle of both line segments
    """
    ..|...
    .-x---
    ..|...
    ......
    """
    line_1_1 = [[2, 1], [2, 3]]
    line_1_2 = [[1, 2], [5, 2]]
    intersection_1 = [2, 2]

    assert intersect(line_1_1, line_1_2) == intersection_1

    # example 2: intersection at the end of one line segment

    """
    ....|.
    ....|.
    ----X-
    """
    line_2_1 = [[0, 0], [5, 0]]
    line_2_2 = [[4, 0], [4, 2]]
    intersection_2 = [4, 0]

    assert intersect(line_2_1, line_2_2) == intersection_2


def test_math_intersect_two_parallel_lines():

    # example 1: parallel line segments
    """
    ....|
    .|..|
    .|..|
    """
    line_1_1 = [[1, 0], [1, 1]]
    line_1_2 = [[4, 0], [4, 2]]

    assert intersect(line_1_1, line_1_2) == None


def test_math_intersect_segments_that_never_meet():

    # example 2: line segments that never meet (although the lines would intersect):
    """
    .....|
    ----.|
    .....|
    """
    line_2_1 = [[0, 1], [3, 1]]
    line_2_2 = [[5, 0], [5, 2]]

    # assert intersect(line_2_1, line_2_2) == None


def test_math_is_in_segment():

    # example 1: overlapping lines
    """
    ..|...
    .-x---
    ..|...
    ......
    """
    line_1_1 = [[2, 1], [2, 3]]
    line_1_2 = [[1, 2], [5, 2]]
    intersection_1 = [2, 2]

    assert is_in_segment(line_1_1, intersection_1) == True
    assert is_in_segment(line_1_2, intersection_1) == True


def test_math_is_in_segment_false():

    # example 1: is in none of the two segments:
    """
    ...---
    ......
    .|....
    .|....
    .|....
    """
    line_1_1 = [[1, 0], [1, 2]]
    line_1_2 = [[3, 4], [5, 4]]
    intersection_1 = [1, 4]

    assert is_in_segment(line_1_1, intersection_1) == False
    assert is_in_segment(line_1_2, intersection_1) == False

    # example 2: is in only one segment:
    """
    .....|
    ----.|
    .....|
    """

    line_2_1 = [[0, 1], [3, 1]]
    line_2_2 = [[5, 0], [5, 2]]
    intersection_2 = [5, 1]

    assert is_in_segment(line_2_1, intersection_2) == False
    assert is_in_segment(line_2_2, intersection_2) == True
