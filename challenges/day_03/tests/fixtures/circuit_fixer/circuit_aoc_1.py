
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

circuit_aoc_1['cables'] = [
    ['R8', 'U5', 'L5', 'D3'],
    ['U7', 'R6', 'D4', 'L4']
]

circuit_aoc_1['dimensions'] = {
    'min_x': 0,
    'max_x': 9,
    'min_y': 0,
    'max_y': 8
}

# circuit_aoc_1['size'] = [10, 9]

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
circuit_aoc_1['occupancy_map'] = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 2, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 1, 1, 2, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
]

circuit_aoc_1['intersections'] = [
    [4, 4],
    [7, 6]
]

circuit_aoc_1['closest_intersection'] = [
    [4, 4],
    6
]
