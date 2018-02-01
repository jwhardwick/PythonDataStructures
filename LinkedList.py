class LinkedList:
    def __init__(self):
        self.head = None
        self.current = self.head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            nextItem = self.current
            self.current = self.current.next
            return nextItem

class ListItem:
    def __init__(self, h, k):
        self.h = h
        self.k = k
        self.next = None
        self.prev = None
