class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


q = Queue()

print q.isEmpty()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue('ok')
print q.dequeue()
print q.dequeue()
print q.size()
print q.dequeue()
print q.dequeue()
print q.isEmpty()
