"""
https://www.interviewcake.com/question/python3/bracket-validator?course=fc1&section=queues-stacks

Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.

Examples:

"{ [ ] ( ) }" should return True
"{ [ ( ] ) }" should return False
"{ [ }" should return False

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


def bracket_validator(s):
    bracket_map = {'{':'}', '(':')', '[':']'}
    stack = []  # stack

    for t in s:
        if t == "{" or t == "(" or t == "[":
            stack.append(bracket_map[t])
        if t == "}" or t == ")" or t == "]":
            if not stack:
                return False
            bracket = stack.pop()
            if t != bracket:
                print('Not valid')
                return False

    if not stack:
        # print('Valid')
        return True


text = "{ [ ] ( ) }"
bracket_validator(text)
