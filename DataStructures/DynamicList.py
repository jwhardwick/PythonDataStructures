from math import pow

class DynamicList:

    def __init__(self):
        self.buckets = [ Bucket(0) ]


    def add(self, data):

        if self.buckets[-1].isFull():
            # We need a new bucket
            self.buckets.append( Bucket(self.buckets[-1].level + 1) )

        # Add to end of bucket
        self.buckets[-1].add(data)
        return True

    def get(self, index):

        # Check upper bound
        if index > 2 ^ (self.buckets[-1].level + 1) - 1:
            return None

        for bucket in reversed(self.buckets):
            start = bucket.capacity - 1
            if index >= start:
                # Item in this bucket
                return bucket.datas[index - start]

        return None


class Bucket:

    def __init__(self, level):
        self.level = level
        self.size = 0
        self.capacity = int(pow(2, self.level))
        self.datas = [ None for _ in range(self.capacity) ]

    def isFull(self):
        return self.size >= self.capacity

    def add(self, data):
        self.datas[self.size] = data
        self.size += 1
