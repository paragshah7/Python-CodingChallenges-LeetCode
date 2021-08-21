"""
Implement a queue with 2 stacks
"""

class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]


class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, item):
        self.s1.push(item)

        # if self.s2.peek() is None:
        #     self.s2.push(item)

    def first_elem(self):
        return self.s2.peek()

    def dequeue(self):
        while self.s1.peek():
            self.s2.push(self.s1.pop())
        first = self.s2.pop()

        while self.s2.peek():
            self.s1.push(self.s2.pop())

        return first


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
# print(q.first_elem())
print(q.dequeue())
print(q.dequeue())
