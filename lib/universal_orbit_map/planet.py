class Planet:

    def __init__(self, name=None, code=None):
        self.name = name
        self.code = code

        self.orbit = []
        self.orbits_list = None

    """
    Simple Getters
    """

    def getName(self):
        return self.name

    def getCode(self):
        return self.code

    def getOrbitsList(self):
        return self.orbits_list

    def getInOrbit(self):
        return self.orbit

    def getTotalNumberOfOrbits(self, count=0):
        total_number_of_orbits = count
        for planet in self.orbit:
            total_number_of_orbits += planet.getTotalNumberOfOrbits(
                count+1)

        return total_number_of_orbits

    """
    Simple Setters
    """

    def putInOrbit(self, planet):
        self.orbit.append(planet)
