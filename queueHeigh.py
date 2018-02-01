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





def reconstructQueue(people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    peopleList = [ ListItem(h, k) for (h,k) in people ]

    outputList = LinkedList()


    # Sort by k, h
    sortedPeople = sorted(peopleList, key=lambda x: (x.k, x.h))

    # for item in sortedPeople:
        # print(item.h, item.k)

    for aItem in sortedPeople:
        # print('dealing with: ', aItem.h, aItem.k)
        if outputList.head is None:
                # print('head is none')
                outputList.head = aItem
                continue
        if aItem.k == 0:
            # Add to end of list
            outputList.current = outputList.head
            for bItem in outputList:
                if bItem.next is None:
                    # print('add to end of list')
                    bItem.next = aItem
                    aItem.prev = bItem
        else:
            counter = 0
            isAdded = False
            outputList.current = outputList.head
            for bItem in outputList:
                # print('comparing ', aItem.h, aItem.k, ' with ', bItem.h, bItem.k)

                if bItem.h >= aItem.h:
                    counter += 1
                # print(counter)
                if counter > aItem.k:
                    isAdded = True
                    # Add before bItem
                    # print('Adding after bItem')
                    prevItem = bItem.prev
                    if prevItem:
                        prevItem.next = aItem
                        aItem.prev = prevItem
                    bItem.prev = aItem
                    aItem.next = bItem
                    break
            if isAdded is False:
                # Add to end of list
                outputList.current = outputList.head
                for bItem in outputList:
                    if bItem.next is None:
                        # print('add to end of list')
                        bItem.next = aItem
                        aItem.prev = bItem

    # outputList.current = outputList.head
    # for item in outputList:
    #     print(item.h, item.k)

    outputList.current = outputList.head
    resultList = [ [item.h, item.k] for item in outputList ]

    return resultList



answer = reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])

print(answer)
