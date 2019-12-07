
class CircuitFixer:

    def __init__(self, circuit):
        self.circuit = circuit

        # init representations of this circuit:
        self.cables = self.initCables()
        self.circuit_dimensions = self.initCircuitDimensions()
        self.occupancy_map = self.initOccupancyMap()

    """
    Getters
    """

    def getCircuit(self):
        return self.circuit

    def getCables(self):
        return self.cables

    def getCircuitDimensions(self):
        return self.circuit_dimensions

    def getOccupancyMap(self):
        return self.occupancy_map

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

    def initCircuitDimensions(self):
        """
        Extracts the dimensions of the circuit.
        Returns an array of min/max values on x/y axis.
        """

        min_x = 0
        min_y = 0
        max_x = 1
        max_y = 1

        for cable in self.cables:

            pos_x = 1
            pos_y = 1

            for command in cable:
                direction = command[0]
                distance = int(command[1:])

                if direction == 'R':
                    pos_x += distance
                    if pos_x > max_x:
                        max_x = pos_x

                elif direction == 'L':
                    pos_x -= distance
                    if pos_x < min_x:
                        min_x = pos_x

                elif direction == 'U':
                    pos_y += distance
                    if pos_y > max_y:
                        max_y = pos_y

                elif direction == 'D':
                    pos_y -= distance
                    if pos_y < min_y:
                        min_y = pos_y

        return {"min_x": min_x, "max_x": max_x, "min_y": min_y, "max_y": max_y}

    def initOccupancyMap(self):
        """
        Returns an occupany map (list of lists x/y) extracted from the list of cables.
        Each field is an integer that indicates how many cables are occupying it.
        """

        # initialize circuit board:

        circuit = [[0 for j in range(self.circuit_dimensions['min_x'], self.circuit_dimensions['max_x'] + 1)]
                   for i in range(self.circuit_dimensions['min_y'], self.circuit_dimensions['max_y'] + 1)]

        for line in circuit:
            print(line)

        # calculate occupancies:
        for cable in self.cables:
            pointer_x = 1
            pointer_y = 1

            for command in cable:
                direction = command[0]
                distance = int(command[1:])
                print(direction + " --> " + str(distance))

                if direction == 'R':
                    for x in range(pointer_x + 1, pointer_x + distance + 1):
                        circuit[pointer_y][x] += 1
                    pointer_x += distance

                elif direction == 'L':
                    print('L')

                elif direction == 'U':
                    for y in range(pointer_y + 1, pointer_y + distance + 1):
                        circuit[y][pointer_x] += 1
                    pointer_y += distance

                elif direction == 'D':
                    print('D')

        # for cable in self.cables:
        #     # print("cable: " + str(cable))
        #     pos_x = 1
        #     pos_y = 1
        #     for command in cable:
        #         direction = command[0]
        #         distance = int(command[1:])

        #         # print("command: " + direction + " -> " + str(distance))

        #         if direction == "R":
        #             # print(str(pos_x) + " : " + str(pos_x + distance))
        #             for x in range(pos_x, pos_x + distance):
        #                 circuit[x][pos_y] += 1
        #             pos_x += distance

        #         elif command[0] == "L":
        #             for x in range(pos_x, pos_x - distance):
        #                 circuit[x][pos_y] -= 1
        #             pos_x -= distance

        #         if direction == "U":
        #             for y in range(pos_y, pos_y + distance):
        #                 circuit[pos_x][y] += 1
        #             pos_y += distance

        #         elif command[0] == "D":
        #             for y in range(pos_y, pos_y - distance):
        #                 circuit[pos_x][y] -= 1
        #             pos_y -= distance

        return circuit

    # def initializeCircuitBoard(self):

    #     circuit = [[0 for j in range(circuit_dimensions['min_y'], circuit_dimensions['max_y'])]
    #            for i in range(circuit_dimensions['min_x'], circuit_dimensions['max_x'])]

    #     self.circuit_board = result

    def getDistanceOfClosestIntersection(self):
        return 42
