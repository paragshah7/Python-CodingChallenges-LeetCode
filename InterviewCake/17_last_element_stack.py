"""
Find largest element in a stack
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


class MaxStack:
    def __init__(self):
        self.stack = Stack()

        """We use a stack to store max because if someone pops a stack and
            that is the max item we need 2nd max to be maintained, stack can do that """
        self.max_num = Stack()

    def push(self, item):
        self.stack.push(item)

        if self.max_num.peek() is None or item >= self.max_num.peek():
            self.max_num.push(item)

    def pop(self):
        item = self.stack.pop()
        if item == self.max_num.peek():
            self.max_num.pop()
        return item

    def get_max(self):
        """The last item in maxes_stack is the max item in our stack."""
        return self.max_num.peek()



s = MaxStack()
s.push(1)
s.push(2)
s.push(10)
s.push(4)
s.push(5)
print(s.get_max())
