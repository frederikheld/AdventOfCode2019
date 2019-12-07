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

    def initList(self):
        return self.code.replace(" ", "").split(",")
