
def get_distance_of_closest_intersection(circuit_diagram):
    cables_raw = circuit_diagram.splitlines()

    # convert to list of lists:
    cables = []
    for cable in cables_raw:
        cables.append(cable.replace(" ", "").split(","))

    # get dimensions of circuit:
    print(get_circuit_dimensions(cables))

    # circuit = []
    # pos_x = 0
    # pos_y = 0

    # for cable in cables:
    #     for command in cable:
    #         direction = command[0]
    #         distance = command[1:]
    #         print(direction + " -> " + distance)
    #         if direction == "R":
    #             for x in range(pos_x, pos_x + distance):
    #                 try:
    #                     circuit(x, pos_y)
    #                 except IndexError:
    #                     circuit[x].append(1)

    # elif command[0] == "D":
    #     print("D")
    # elif command[0] == "L":
    #     print("L")
    # elif command[0] == "U":
    #     print("U")

    # print(circuit)


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
