
"""
Prepare different representations of circuit_1.
ciruit_1 contains only movements in positive directions (right and up).
"""

#     """
#     ....|..
#     .+--x--
#     .0--+..
#     .......
#     """

circuit_1 = {}

circuit_1['raw'] = """ \
R3, U2
U1, R5
"""

circuit_1['cables'] = [
    ['R3', 'U2'],
    ['U1', 'R5']
]

circuit_1['dimensions'] = {
    'min_x': 0,
    'max_x': 6,
    'min_y': 0,
    'max_y': 3
}

# circuit_1['size'] = [7, 4]

circuit_1['occupancy_map'] = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 2, 1, 1],
    [0, 0, 0, 0, 1, 0, 0]
]