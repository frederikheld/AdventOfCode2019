
"""
Prepare different representations of circuit_2.
ciruit_2 contains movements in all directions (right, up, left and down)
and 2 intersections
"""


"""
..+---+
.-x--+|
..|.-x+
..o--+.
"""

circuit_2 = {}

circuit_2['raw'] = """ \
R3, U2, L4
U3, R4, D2, L2
"""

circuit_2['start'] = [2, 0]

circuit_2['cables'] = [
    ['R3', 'U2', 'L4'],
    ['U3', 'R4', 'D2', 'L2']
]

circuit_2['intersections'] = [
    [5, 1],
    [2, 2]
]

circuit_2['closest_intersection'] = [
    [2, 2],
    2
]
