
def calculate_manhattan_distance(start, end):
    distance_x = end[0] - start[0]
    if end[0] < start[0]:
        distance_x = start[0] - end[0]

    distance_y = end[1] - start[1]
    if end[1] < start[1]:
        distance_y = start[1] - end[1]

    return distance_x + distance_y
