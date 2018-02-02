
class LinkedList:
    def __init__(self):
        self.front = None
        self._size = 0

    def sizeOf(self):
        return self._size

    def add(self, data):
        newListItem = self.ListItem(data)

        # Empty List
        if self.isEmpty():
            self.front = newListItem
        else:
            head = self.front
            while head.next != None:
                head = head.next
            head.next = newListItem
            newListItem.prev = head
        self._size += 1

    def isEmpty(self):
        return self._size == 0

    def contains(self, data):
        if self.isEmpty():
            return False

        head = self.front
        while head != None:
            if head.data == data:
                return True
            head = head.next
        return False

    def remove(self, data):
        if self.isEmpty():
            return

        head = self.front
        while head != None:
            if head.data == data:
                  if self.front == head:
                      self.front = head.next
                      if self.front:
                          self.front.prev = None
                  else:
                      prevItem = head.prev
                      prevItem.next = head.next
                      prevItem.next.prev = prevItem
                  return

    def __getitem(self, key):
        return
    class ListItem:
        def __init__(self, data):
            self.next = None
            self.prev = None
            self.data = data

