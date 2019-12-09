from . import math_geometry


class Cable:
    def __init__(self, code, start=[0, 0]):
        self.code = code
        self.start = start

        # init representations of this cable:
        self.list = self.initList()
        self.sections = self.initSections()

    """
    Simple Getters
    """

    def getCode(self):
        return self.code

    def getStart(self):
        return self.start

    def getList(self):
        return self.list

    def getSections(self):
        return self.sections

    """
    Advanced Getters
    """

    """
    Functions that calculate different representations
    of the cable from its code on on initialization.
    """

    def initList(self):
        return self.code.replace(" ", "").split(",")

    def initSections(self):

        sections = []

        pointer_x = self.start[0]
        pointer_y = self.start[1]

        for command in self.list:
            direction = command[0]
            distance = int(command[1:])

            section = []
            section.append([pointer_x, pointer_y])

            if direction == 'R':
                pointer_x += distance

            elif direction == 'L':
                pointer_x -= distance

            elif direction == 'U':
                pointer_y += distance

            elif direction == 'D':
                pointer_y -= distance

            section.append([pointer_x, pointer_y])

            sections.append(section)

        return sections

    """
    The real shit
    """

    def getDistanceAlongCable(self, point):
        """
        Returns distance along cable from start to the given point.
        Returns None if point is not on cable.
        """

        print("start: " + str(self.start) + " -> point: " + str(point))
        print(self.list)

        pointer_x = self.start[0]
        pointer_y = self.start[1]

        distance_along_cable = 0

        # edge case: self.start == point:
        if [pointer_x, pointer_y] == point:
            return distance_along_cable

        for command in self.list:
            direction = command[0]
            distance = int(command[1:])

            if direction == 'R':
                for x in range(distance):
                    pointer_x += 1
                    distance_along_cable += 1
                    if [pointer_x, pointer_y] == point:
                        return distance_along_cable

            elif direction == 'L':
                for x in range(distance):
                    pointer_x -= 1
                    distance_along_cable += 1
                    if [pointer_x, pointer_y] == point:
                        return distance_along_cable

            elif direction == 'U':
                for y in range(distance):
                    pointer_y += 1
                    distance_along_cable += 1
                    if [pointer_x, pointer_y] == point:
                        return distance_along_cable

            elif direction == 'D':
                for y in range(distance):
                    pointer_y -= 1
                    distance_along_cable += 1
                    if [pointer_x, pointer_y] == point:
                        return distance_along_cable

        return None

    def intersect(self, other_cable):
        intersections = []
        for section in self.sections:
            for other_section in other_cable.getSections():
                intersection = math_geometry.intersect_segments(
                    section, other_section)
                if intersection:
                    intersections.append(intersection)

        if len(intersections) > 0:
            return intersections

        return None
