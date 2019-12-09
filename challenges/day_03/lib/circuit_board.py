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
                        intersection_detailled = []
                        for intersection in cable_intersections:
                            intersection_detailled.append({
                                'coordinates': intersection,
                                'cable_1': cable,
                                'cable_2': cable_2
                            })
                        intersections += intersection_detailled
        # TODO: This can be done more efficiently with drawing without placing back.
        #       Right now all intersections are calculate twice because both cables
        #       are run through the algorithm.
        #       This would also make removing duplicates (see belwo) unnecessary.

        result = []
        temp_intersections = []
        for intersection in intersections:

            # ignore start point:
            if intersection['coordinates'] == self.start:
                continue

            # ignore duplicates:
            if intersection['coordinates'] in temp_intersections:
                continue

            result.append(intersection)
            temp_intersections.append(intersection['coordinates'])

        return result

    def getClosestIntersection(self):
        closest_intersection = None
        lowest_distance = None

        for intersection in self.getIntersections():

            calculated_manhattan_distance = math_geometry.calculate_manhattan_distance(
                self.start, intersection['coordinates'])

            if lowest_distance == None or calculated_manhattan_distance < lowest_distance:
                lowest_distance = calculated_manhattan_distance
                closest_intersection = [
                    intersection['coordinates'],
                    calculated_manhattan_distance
                ]

        return closest_intersection

    def getClosestIntersectionAlongCables(self):
        closest_intersection = None
        lowest_distance = None

        for intersection in self.getIntersections():

            calculated_distance_along_cables = intersection['cable_1'].getDistanceAlongCable(
                intersection['coordinates']) + intersection['cable_2'].getDistanceAlongCable(intersection['coordinates'])

            if lowest_distance == None or calculated_distance_along_cables < lowest_distance:
                lowest_distance = calculated_distance_along_cables
                closest_intersection = [
                    intersection['coordinates'],
                    calculated_distance_along_cables
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
