class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[i // 2]
                self.heapList[i // 2] = tmp
            i //= 2

    def insert(self, k):
        print 'About to insert..', k
        self.heapList.append(k)
        self.display()
        self.currentSize += 1
        self.percUp(self.currentSize)
        print 'Heap after inserting', self.display()

    def minChild(self, i):
        if i * 2 + 1 < self.currentSize:
            return i * 2
        else:

            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percDown(self, i):
        while i * 2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def display(self):
        print self.heapList[1:]


heap = BinHeap()
heap.insert(9)
heap.insert(5)
heap.insert(2)
heap.insert(1)
heap.insert(4)
heap.insert(3)

heap.display()
