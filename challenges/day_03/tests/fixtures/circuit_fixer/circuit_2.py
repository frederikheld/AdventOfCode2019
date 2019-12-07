
"""
Prepare different representations of circuit_2.
ciruit_1 contains only movements in positive directions (right and up).
"""


#     """
#     .+---+
#     -x--+|
#     .|..||
#     .0--+.
#     ......
#     """

circuit_2 = {}

circuit_2['raw'] = """ \
R3, U2, L4
U3, R4, D2
"""

circuit_2['cables'] = [
    ['R3', 'U2', 'L4'],
    ['U3', 'R4', 'D2']
]

circuit_2['dimensions'] = {
    'min_x': 0,
    'max_x': 5,
    'min_y': 0,
    'max_y': 4
}

# circuit_2['size'] = [6, 5]

circuit_2['occupancy_map'] = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 1],
    [1, 2, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1]
]
