from .cable import Cable


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
