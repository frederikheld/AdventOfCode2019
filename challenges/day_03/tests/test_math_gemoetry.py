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
    line_1_1 = [[2, 1], [2, 3]]
    line_1_2 = [[1, 2], [5, 2]]
    intersection_1 = [2, 2]

    assert intersect_lines(line_1_1, line_1_2) == intersection_1

    # example 2:

    """
    ....|.
    ....|.
    ----X-
    """
    line_2_1 = [[0, 0], [5, 0]]
    line_2_2 = [[4, 0], [4, 2]]
    intersection_2 = [4, 0]

    assert intersect_lines(line_2_1, line_2_2) == intersection_2

    # example 3:
    """
    .....|
    ----.|
    .....|
    """
    line_3_1 = [[0, 1], [3, 1]]
    line_3_2 = [[5, 0], [5, 2]]
    intersection_3 = [5, 1]

    assert intersect_lines(line_3_1, line_3_2) == intersection_3


def test_math_intersect_two_parallel_lines():

    # example 1: parallel lines
    """
    ....|
    .|..|
    .|..|
    """
    line_1_1 = [[1, 0], [1, 1]]
    line_1_2 = [[4, 0], [4, 2]]

    assert intersect_lines(line_1_1, line_1_2) == None


def test_math_intersect_two_segments():

    # example 1: intersection in the middle of both line segments
    """
    ..|...
    .-x---
    ..|...
    ......
    """
    segment_1_1 = [[2, 1], [2, 3]]
    segment_1_2 = [[1, 2], [5, 2]]
    intersection_1 = [2, 2]

    assert intersect_segments(segment_1_1, segment_1_2) == intersection_1

    # example 2: intersection at the end of one line segment:

    """
    ....|.
    ....|.
    ----X-
    """
    segment_2_1 = [[0, 0], [5, 0]]
    segment_2_2 = [[4, 0], [4, 2]]
    intersection_2 = [4, 0]

    assert intersect_segments(segment_2_1, segment_2_2) == intersection_2

    # example 3: no intersection within the two segments:
    """
    .....|
    ----.|
    .....|
    """
    segment_3_1 = [[0, 1], [3, 1]]
    segment_3_2 = [[5, 0], [5, 2]]

    assert intersect_segments(segment_3_1, segment_3_2) == None

    # example 4: touching segments with no intersection within the two segments:
    """
    ------
    ..|...
    ..|...
    ..|...
    """
    segment_4_1 = [[2, 0], [2, 2]]
    segment_4_2 = [[0, 3], [5, 3]]

    assert intersect_segments(segment_4_1, segment_4_2) == None


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

    # example 3: lines touch but don't intersect:
    """
    ...|..
    ...|..
    ..----
    ......
    """

    line_3_1 = [[2, 1], [5, 1]]
    line_3_2 = [[3, 2], [3, 3]]
    intersection_3 = [3, 1]

    assert is_in_segment(line_3_1, intersection_3) == True
    assert is_in_segment(line_3_2, intersection_3) == False

    # example 4: lines touch but don't intersect:
    """
    .-----
    ...|..
    ...|..
    ...|..
    """

    line_4_1 = [[3, 0], [3, 2]]
    line_4_2 = [[1, 3], [5, 3]]
    intersection_4 = [3, 3]

    assert is_in_segment(line_4_1, intersection_4) == False
    assert is_in_segment(line_4_2, intersection_4) == True
