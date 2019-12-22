class Planet:

    def __init__(self, name, code=None):

        # has a name:
        self.name = name

        # can have code that describes the map of this planet
        # in relation to the planets in its orbit:
        self.code = code

        # can have many planets in orbit:
        self.planetsInOwnOrbit = []

        # can be in orbit of exactly one planet:
        self.inOrbitOf = None

    """
    Getters
    """

    def getName(self):
        return self.name

    def getCode(self):
        return self.code

    def getPlanetsInOwnOrbit(self):
        return self.planetsInOwnOrbit

    def getInOrbitOf(self):
        return self.inOrbitOf

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

    def initOrbitsFromCode(self):
        orbits = self.__convertCodeToDict()

        for planet_name in orbits[self.name]:
            self.putInOwnOrbit(Planet(planet_name, orbits[planet_name]))

    """
    Helpers
    """

    def convertCodeToDict(self):

        orbitsList = {}

        for orbit in self.code.splitlines():
            pair = orbit.replace(" ", "").split(")")

            print(pair)

            if pair[0] not in orbitsList:
                orbitsList[pair[0]] = []

            orbitsList[pair[0]].append(pair[1])

        return orbitsList
