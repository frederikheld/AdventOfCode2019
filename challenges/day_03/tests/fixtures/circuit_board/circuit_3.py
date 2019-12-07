
"""
Prepare different representations of circuit_3.
ciruit_3 contains 3 cables.
"""

"""
....|..
.+--x--
.o--+..
.+----.
"""

circuit_3 = {}

circuit_3['raw'] = """ \
R3, U2
U1, R5,
D1, R4
"""

circuit_3['cables'] = [
    ['R3', 'U2'],
    ['U1', 'R5'],
    ['D1', 'R4']
]

circuit_3['intersections'] = [
    [4, 2]
]

circuit_3['closest_intersection'] = [
    [4, 2],
    4
]
