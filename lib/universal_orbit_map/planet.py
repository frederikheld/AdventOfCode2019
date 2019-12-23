class Planet:

    def __init__(self, name):

        # has a name:
        self.name = name

        # can have many planets in orbit:
        self.planetsInOwnOrbit = []

        # can be in orbit of exactly one planet:
        self.inOrbitOf = None

    """
    Getters
    """

    def getName(self):
        return self.name

    def getPlanetsInOwnOrbit(self):
        return self.planetsInOwnOrbit

    def getInOrbitOf(self):
        return self.inOrbitOf

    """
    Advanced Getters
    """

    def getTotalNumberOfOrbits(self, count=0):
        total_number_of_orbits = count
        for planet in self.planetsInOwnOrbit:
            total_number_of_orbits += planet.getTotalNumberOfOrbits(
                count+1)

        return total_number_of_orbits

    """
    Simple Setters
    """

    def putInOrbitOf(self, planet):
        self.inOrbitOf = planet

        if self not in planet.getPlanetsInOwnOrbit():
            planet.putInOwnOrbit(self)

    def putInOwnOrbit(self, planet):
        self.planetsInOwnOrbit.append(planet)

        planet.putInOrbitOf(self)

    """
    Functions that init different represenation of the orbit
    map from the given code
    """

    def initOrbitsFromCode(self, code):
        orbitsDict = self.convertCodeToDict(code)
        self.initOrbitsFromDict(orbitsDict)

    def initOrbitsFromDict(self, orbitsDict):
        print(orbitsDict)
        if orbitsDict:
            for planet_name in orbitsDict[self.name]:
                new_planet = Planet(planet_name)

                if planet_name in orbitsDict:
                    new_planet.initOrbitsFromDict(orbitsDict)

                self.putInOwnOrbit(new_planet)

    """
    Helpers
    """

    def convertCodeToDict(self, code):

        orbitsList = {}

        for orbit in code.splitlines():
            pair = orbit.replace(" ", "").split(")")

            if pair[0] not in orbitsList:
                orbitsList[pair[0]] = []

            orbitsList[pair[0]].append(pair[1])

        return orbitsList
