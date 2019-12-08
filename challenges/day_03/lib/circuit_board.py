from .cable import Cable
from . import math_geometry


class CircuitBoard:

    def __init__(self, code, start=[1, 1]):
        self.code = code
        self.start = start

        # init representations of this cable:
        self.cables = self.initCables()

    """
    Basic Getters
    """

    def getCode(self):
        return self.code

    def getStart(self):
        return self.start

    def getCables(self):
        return self.cables

    """
    Advanced Getters
    """

    def getIntersections(self):
        intersections = []

        # intersect all cables with each others:
        for cable in self.cables:
            for cable_2 in self.cables:
                if cable != cable_2:
                    cable_intersections = cable.intersect(cable_2)

                    if cable_intersections != None:
                        intersections += cable_intersections
        # TODO: This can be done more efficiently with drawing without placing back.
        #       Right now all intersections are calculate twice because both cables
        #       are run through the algorithm.

        # remove duplicates:
        result = []
        for point in intersections:
            if point not in result:
                result.append(point)
        intersections = result

        # remove start point:
        intersections.remove(self.start)

        return intersections

    def getClosestIntersection(self):
        closest_intersection = None
        lowest_distance = None

        for intersection in self.getIntersections():

            calculated_distance = math_geometry.calculate_manhattan_distance(
                self.start, intersection)

            if lowest_distance == None or calculated_distance < lowest_distance:
                lowest_distance = calculated_distance
                closest_intersection = [
                    intersection,
                    calculated_distance
                ]

        return closest_intersection

    """
    Functions that calculate different representations of the
    circuit from the raw circuit
    """

    def initCables(self):
        """
        Returns a list of cables extracted from the raw circuit.
        Each cable is a list of the corresponding raw commands.
        """

        cables = []

        for cable in self.code.splitlines():
            cables.append(Cable(cable, self.start))

        return cables
