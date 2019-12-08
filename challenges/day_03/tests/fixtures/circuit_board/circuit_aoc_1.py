
"""
First example circuit from the aoc website (https://adventofcode.com/2019/day/3).
"""

"""
...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
"""

circuit_aoc_1 = {}

circuit_aoc_1['raw'] = """ \
R8,U5,L5,D3
U7,R6,D4,L4
"""

circuit_aoc_1['start'] = [1, 1]

circuit_aoc_1['cables'] = [
    ['R8', 'U5', 'L5', 'D3'],
    ['U7', 'R6', 'D4', 'L4']
]

circuit_aoc_1['intersections'] = [
    [4, 4],
    [7, 6]
]

circuit_aoc_1['closest_intersection'] = [
    [4, 4],
    6
]

circuit_aoc_1['closest_intersection_along_cables'] = [
    [4, 4],
    30
]
