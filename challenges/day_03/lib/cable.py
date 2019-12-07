class Cable:
    def __init__(self, cable, start=[0, 0]):
        self.code = cable
        self.start = start

        # init representations of this cable:

        self.list = self.initList()

    """
    Simple Getters
    """

    def getCode(self):
        return self.code

    def getStart(self):
        return self.start

    def getList(self):
        return self.list

    """
    Advanced Getters
    """

    """
    Functions that calculate different representations
    of the cable from its code.
    """

    def initList(self):
        return self.code.replace(" ", "").split(",")

    def initSections(self):

        sections = []

        pointer_x = self.start[0]
        pointer_y = self.start[1]

        for command in self.list:
            direction = command[0]
            distance = int(command[1:])

            section = []
            section.append([pointer_x, pointer_y])

            if direction == 'R':
                pointer_x += distance

            elif direction == 'L':
                pointer_x -= distance

            elif direction == 'U':
                pointer_y += distance

            elif direction == 'D':
                pointer_y -= distance

            section.append([pointer_x, pointer_y])

            print(section)

            sections.append(section)

        return sections
