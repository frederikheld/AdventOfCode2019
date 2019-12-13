class Planet:

    def __init__(self, name=None):
        self.name = name
        self.orbit = []

    """
    Simple Getters
    """

    def getName(self):
        return self.name

    def getInOrbit(self):
        return self.orbit

    def getTotalNumberOfOrbits(self, count=0):
        total_number_of_orbits = count
        for planet in self.orbit:
            # if (len(planet.getInOrbit()) > 0):
            total_number_of_orbits += planet.getTotalNumberOfOrbits(
                count+1)
            # else:
            #     total_number_of_orbits += 1

        return total_number_of_orbits

    """
    Simple Setters
    """

    def putInOrbit(self, planet):
        self.orbit.append(planet)

    # def append(self, next):
    #     self.next.append(next)
    #     if self not in next.getPrev():
    #         next.prepend(self)

    # def prepend(self, prev):
    #     self.prev.append(prev)
    #     if self not in prev.getNext():
    #         prev.append(self)
    """
    List Traversing
    """

    # def getList(self, reversed=False):
    #     list = []
    #     list.append(self.value)
    #     if self.prev:
    #         list += self.prev.getList()

    #     if reversed:
    #         list.reverse()

    #     return list
