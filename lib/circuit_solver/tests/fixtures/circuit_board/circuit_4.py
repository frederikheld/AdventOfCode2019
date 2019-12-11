
"""
Prepare different representations of circuit_4.
circuit_4's closest intersection in manhattan distance
is different from it's closest intersection along the cables.
"""


"""
..+---+.
..|...|.
.+x---x-
.||...|.
.o----+.
........
"""

circuit_4 = {}

circuit_4['raw'] = """ \
U2, R6
R5, U4, L4, D3
"""

circuit_4['start'] = [1, 1]

circuit_4['intersections'] = [
    [2, 3],
    [6, 3]
]

circuit_4['closest_intersection'] = [
    [2, 3],
    3
]

circuit_4['closest_intersection_along_cables'] = [
    [6, 3],
    14
]
