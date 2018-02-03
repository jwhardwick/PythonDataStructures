import unittest
from LinkedList import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.link = LinkedList()

    def testAdd(self):
        self.link.add(0)
        self.assertEqual(self.link.sizeOf(), 1, 'Incorrect size after add')
        for i in range(1,10):
            self.link.add(i)
        self.assertEqual(self.link.sizeOf(), 10, 'Incorrect size after adding multiple objects')

    def testContains(self):
        self.testAdd()
        for i in range(10):
            self.assertTrue(self.link.contains(i), 'contains() not returning True for an object in the list')

        self.assertFalse(self.link.contains(11), 'contains() returning a false positive')

    def testRemove(self):
        self.testAdd()
        for i in range(10):
            self.link.remove(i)

        self.assertTrue(self.link.isEmpty(), 'All items not removed')

        self.link.add('Test')
        self.assertTrue(self.link.contains('Test'))
        self.assertTrue(self.link.remove('Test'))
        self.assertFalse(self.link.contains('Test'))
        self.assertTrue(self.link.isEmpty())

if __name__ == '__main__':
        unittest.main()
