class CircuitBoard:

    def __init__(self, circuit):
        self.circuit = circuit

        self.cables = self.initCables()

    """
    Basic Getters
    """

    def getCircuit(self):
        return self.circuit

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

        cables_raw = self.circuit.splitlines()

        for cable in cables_raw:
            cables.append(cable.replace(" ", "").split(","))

        return cables
