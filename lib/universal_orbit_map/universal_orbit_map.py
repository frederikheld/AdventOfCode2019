class UniversalOrbitMap:

    def __init__(self, code, universal_center_of_mass='COM'):
        self.code = code
        self.universal_center_of_mass = universal_center_of_mass

        # init representations of this uom:
        self.list = self.initList()
        self.orbits = self.initOrbits()

    """
    Simple Getters
    """

    def getCode(self):
        return self.code

    def getList(self):
        return self.list

    def getOrbits(self):
        return self.orbits

    def getUniversalCenterOfMass(self):
        return self.universal_center_of_mass

    """
    Simple Setters
    """

    """
    Functions that calculate different representations of the
    map from the given code
    """

    def initList(self):
        """
        Returns a list of cables extracted from the raw circuit.
        Each cable is a list of the corresponding raw commands.
        """

        orbits_list = {}

        for line in self.code.splitlines():
            orbit_definition = line.replace(" ", "").split(')')

            if orbit_definition[0] in orbits_list.keys():
                orbits_list[orbit_definition[0]].append(orbit_definition[1])
            else:
                orbits_list[orbit_definition[0]] = [orbit_definition[1]]

        return orbits_list

    def initOrbits(self):
        """
        Has to be called after self.initList()!
        """

        # orbits
