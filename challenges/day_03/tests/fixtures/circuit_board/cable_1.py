"""
...|
+--x
o--+
"""

cable_1 = {}

cable_1['code'] = 'R3, U2'

cable_1['start'] = [0, 0]

cable_1['list'] = ['R3', 'U2']

cable_1['sections'] = [
    [
        [0, 0],
        [3, 0]
    ],
    [
        [3, 0],
        [3, 2]
    ]
]


cable_1_1 = {}

cable_1_1['code'] = 'U1, R3'

cable_1_1['start'] = [0, 0]

cable_1_1['sections'] = [
    [
        [0, 0],
        [3, 0]
    ],
    [
        [3, 0],
        [3, 2]
    ]
]


cable_1['intersections'] = [
    [0, 0],
    [3, 1]
]
