def get_distance_of_closest_intersection(circuit_diagram):
    cables_raw = circuit_diagram.splitlines()

    # convert to list of lists:
    cables = []
    for cable in cables_raw:
        cables.append(cable.replace(" ", "").split(","))

    # get dimensions of circuit:
    circuit_dimensions = get_circuit_dimensions(cables)

    # initialize circuit board:
    circuit = [[0 for j in range(circuit_dimensions['min_y'], circuit_dimensions['max_y'])]
               for i in range(circuit_dimensions['min_x'], circuit_dimensions['max_x'])]

    for cable in cables:
        print("cable: " + str(cable))
        pos_x = 1
        pos_y = 1
        for command in cable:
            direction = command[0]
            distance = int(command[1:])

            print("command: " + direction + " -> " + str(distance))

            if direction == "R":
                print(str(pos_x) + " : " + str(pos_x + distance))
                for x in range(pos_x, pos_x + distance):
                    circuit[x][pos_y] += 1
                pos_x += distance

            elif command[0] == "L":
                for x in range(pos_x, pos_x - distance):
                    circuit[x][pos_y] -= 1
                pos_x -= distance

            if direction == "U":
                for y in range(pos_y, pos_y + distance):
                    circuit[pos_x][y] += 1
                pos_y += distance

            elif command[0] == "D":
                for y in range(pos_y, pos_y - distance):
                    circuit[pos_x][y] -= 1
                pos_y -= distance

            for line in circuit:
                print(line)
            print("\n")

    for line in circuit:
        print(line)

    intersections = get_intersections(circuit)

    print(intersections)


def get_intersections(circuit):
    result = []
    for x in range(len(circuit)):
        for y in range(len(circuit[0])):
            if (circuit[x][y] > 1):
                result.append([x, y])

    return result


def get_circuit_dimensions(cables):
    min_x = 0
    min_y = 0
    max_x = 1
    max_y = 1

    for cable in cables:

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
