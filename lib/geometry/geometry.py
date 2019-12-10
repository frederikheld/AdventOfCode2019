def intersect_segments(segment1, segment2):
    intersection = intersect_lines(segment1, segment2)

    if intersection:
        if is_in_segment(segment1, intersection) and is_in_segment(segment2, intersection):
            return intersection

    return None


def intersect_lines(line1, line2):
    """
    Calculates the intersection between two line segments
    that are defined by their start and end point.
    """

    x1 = line1[0][0]
    y1 = line1[0][1]
    x2 = line1[1][0]
    y2 = line1[1][1]

    x3 = line2[0][0]
    y3 = line2[0][1]
    x4 = line2[1][0]
    y4 = line2[1][1]

    try:
        xi = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / \
            ((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))

        yi = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / \
            ((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))

    except ZeroDivisionError:
        return None

    return [int(xi), int(yi)]


def is_in_segment(segment, point):
    """
    Calculates if the given points
    lies in the given segment.
    """

    dxc = point[0] - segment[0][0]
    dyc = point[1] - segment[0][1]

    dx1 = segment[1][0] - segment[0][0]
    dy1 = segment[1][1] - segment[0][1]

    is_point_on_line = False

    cross_product = dxc * dy1 - dyc * dx1
    if cross_product == 0:
        is_point_on_line = True

    is_point_in_segment = False
    if abs(dx1) >= abs(dy1):
        if dx1 > 0:
            is_point_in_segment = segment[0][0] <= point[0] and point[0] <= segment[1][0]
        else:
            is_point_in_segment = segment[1][0] <= point[0] and point[0] <= segment[0][0]

    else:
        if dy1 > 0:
            is_point_in_segment = segment[0][1] <= point[1] and point[1] <= segment[1][1]
        else:
            is_point_in_segment = segment[1][1] <= point[1] and point[1] <= segment[0][1]

    if is_point_on_line and is_point_in_segment:
        return True

    return False


def calculate_manhattan_distance(point1, point2):
    distance_x = point2[0] - point1[0]
    if point2[0] < point1[0]:
        distance_x = point1[0] - point2[0]

    distance_y = point2[1] - point1[1]
    if point2[1] < point1[1]:
        distance_y = point1[1] - point2[1]

    return abs(distance_x) + abs(distance_y)
