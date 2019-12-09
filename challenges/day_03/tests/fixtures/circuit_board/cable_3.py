"""
cable_3 intersects with cable_3_1 after doing turns in all 4 directions.
"""

"""
.+----+.
.|....|.
.|.o--+.
.|.++...
.+--x---
"""

cable_3 = {}

cable_3['code'] = 'R3, U2, L5, D4, R6'

cable_3['start'] = [3, 2]


cable_3_1 = {}

cable_3_1['code'] = 'D1, R1, D1'

cable_3_1['start'] = [3, 2]


cable_3['intersections'] = [
    [3, 2],
    [4, 0]
]

cable_3['distance_along_cable'] = [
    0,
    17
]
