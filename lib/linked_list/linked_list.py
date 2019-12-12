class ListNode:

    def __init__(self, value=None, prev=None):
        self.value = value
        self.prev = prev

    """
    Simple Getters
    """

    def getValue(self):
        return self.value

    def getPrev(self):
        return self.prev

    """
    Simple Setters
    """

    def setPrev(self, prev):
        self.prev = prev

    """
    List Traversing
    """

    def getList(self):
        list = []
        list.append(self.value)
        if self.prev:
            list += self.prev.getList()

        return list
