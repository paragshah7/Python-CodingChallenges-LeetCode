"""
Implement stack
"""

class Stack():
    def __init__(self):
        self.values = []

    def is_empty(self):
        return len(self.values) == 0

    def push(self, value):
        self.values.append(value)
        print(value, 'pushed')

    def pop(self):
        if not self.is_empty():
            popped_elem = self.values.pop()
            print(popped_elem, 'popped')
        else:
            print("stack empty")

    def print_stack(self):
        print(self.values, "<-- top")


    def peek(self):
        if not self.is_empty():
            print(self.values[-1], "<-- top")
        else:
            print("stack empty")


s = Stack()
s.pop()
s.push(1)
s.push(2)
s.pop()
s.push(3)
s.push(4)
s.push(5)
s.pop()
s.print_stack()
s.peek()
