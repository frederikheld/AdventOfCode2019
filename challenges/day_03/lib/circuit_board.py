from .cable import Cable


class CircuitBoard:

    def __init__(self, circuit):
        self.code = circuit

        self.cables = self.initCables()

    """
    Basic Getters
    """

    def getCode(self):
        return self.code

    def getCables(self):
        return self.cables

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
            cables.append(Cable(cable))

        return cables
