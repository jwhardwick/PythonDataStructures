
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

        prev = None
        curr = self.front

        while curr:
            if curr.data == data:
                if prev:
                    prev.next = curr.next
                else:
                    self.front = curr.next
                self._size -= 1
                return True

            prev = curr
            curr = curr.next

        return False


    def __getitem(self, key):
        return
    class ListItem:
        def __init__(self, data):
            self.next = None
            self.prev = None
            self.data = data

