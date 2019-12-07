
"""
Prepare different representations of circuit_1.
ciruit_1 contains only movements in positive directions (right and up).
"""

"""
....|..
.+--x--
.o--+..
.......
"""

circuit_1 = {}

circuit_1['raw'] = """ \
R3, U2
U1, R5
"""

circuit_1['cables'] = [
    ['R3', 'U2'],
    ['U1', 'R5']
]

circuit_1['intersections'] = [
    [4, 2]
]

circuit_1['closest_intersection'] = [
    [4, 2],
    4
]
