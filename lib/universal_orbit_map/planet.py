class Planet:

    def __init__(self, name, orbitsDict=None):

        # has a name:
        self.name = name

        # can have a dictionary that describes the planets
        # in own orbit:
        self.orbitsDict = orbitsDict

        # can have many planets in orbit:
        self.planetsInOwnOrbit = []

        # can be in orbit of exactly one planet:
        self.inOrbitOf = None

        self.initOrbitsFromDict()

    """
    Getters
    """

    def getName(self):
        return self.name

    def getOrbitsDict(self):
        return self.orbitsDict

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

    def initOrbitsFromCode(self, code):
        self.orbitsDict = self.convertCodeToDict(code)
        self.initOrbitsFromDict()

    def initOrbitsFromDict(self):
        if self.orbitsDict:
            for planet_name in self.orbitsDict[self.name]:
                if planet_name in self.orbitsDict:
                    self.putInOwnOrbit(
                        Planet(planet_name, {planet_name: self.orbitsDict[planet_name]}))
                else:
                    self.putInOwnOrbit(Planet(planet_name))

    """
    Helpers
    """

    def convertCodeToDict(self, code):

        orbitsList = {}

        for orbit in code.splitlines():
            pair = orbit.replace(" ", "").split(")")

            print(pair)

            if pair[0] not in orbitsList:
                orbitsList[pair[0]] = []

            orbitsList[pair[0]].append(pair[1])

        return orbitsList
