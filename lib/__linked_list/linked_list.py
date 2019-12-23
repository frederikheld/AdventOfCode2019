class ListNode:

    def __init__(self, value=None):
        self.value = value
        self.next = []
        self.prev = []

    """
    Simple Getters
    """

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    """
    Simple Setters
    """

    def append(self, next):
        self.next.append(next)
        if self not in next.getPrev():
            next.prepend(self)

    def prepend(self, prev):
        self.prev.append(prev)
        if self not in prev.getNext():
            prev.append(self)

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
