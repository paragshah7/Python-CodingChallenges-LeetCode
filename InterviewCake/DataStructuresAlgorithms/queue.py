"""
Implement queue
"""

class Queue:
    def __init__(self):
        self.values = []

    def is_empty(self):
        return len(self.values) == 0

    def enqueue(self, value):
        self.values.append(value)
        # print(value, 'enqueued')

    # O(n)
    def dequeue(self):
        if not self.is_empty():
            popped_elem = self.values.pop(0)
            # print(popped_elem, 'popped')
            return popped_elem

    def print_queue(self):
        if not self.is_empty():
            print('front -->', self.values, '<-- rear')
        else:
            print('queue empty')

    def peek(self):
        if not self.is_empty():
            print('front -->', self.values[0], '--', self.values[-1], '<-- rear')
        else:
            print('queue empty')


# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.print_queue()
# q.peek()
# q.dequeue()
# q.print_queue()
