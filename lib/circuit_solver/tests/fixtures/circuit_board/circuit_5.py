
"""
Prepare different representations of circuit_5.
ciruit_5 contains 3 cables.
Cable 1 and 2 intersect at one position
and cable 2 and 3 intersect at anoter position
"""

"""
....|.|
.+--x-x
.o--+.|
.+----+
"""

circuit_5 = {}

circuit_5['start'] = [1, 1]

circuit_5['raw'] = """ \
R3, U2
U1, R5
D1, R5, U3
"""

circuit_5['cables'] = [
    ['R3', 'U2'],
    ['U1', 'R5'],
    ['D1', 'R5', 'U3']
]

circuit_5['intersections'] = [
    {
        'coordinates': [4, 2]
    },
    {
        'coordinates': [6, 2]
    }
]

circuit_5['closest_intersection'] = [
    [4, 2],
    4
]
