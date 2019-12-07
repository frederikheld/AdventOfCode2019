class Cable:
    def __init__(self, cable):
        self.code = cable

        # init representations of this cable:

        self.list = self.initList()

    """
    Simple Getters
    """

    def getCode(self):
        return self.code

    def getList(self):
        return self.list

    """
    Advanced Getters
    """

    def initList(self):
        return self.code.replace(" ", "").split(",")
