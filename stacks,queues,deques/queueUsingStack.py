class QueueUsingStack(object):
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, item):
        self.instack.append(item)

    def dequeue(self):
        if len(self.outstack) == 0:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()


q = QueueUsingStack()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue('ok')
print q.dequeue()
print q.dequeue()
