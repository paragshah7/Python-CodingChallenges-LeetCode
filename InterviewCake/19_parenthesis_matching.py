"""
"Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

Write a function that, given a sentence like the one above, along with the position of an opening parenthesis,
finds the corresponding closing parenthesis.

Example: if the example string above is input with the number 10 (position of the first parenthesis),
the output should be 79 (position of the last parenthesis).
"""
from DataStructuresAlgorithms.stack import Stack

def parenthesis_matching(text, inp_in):
    s = Stack()

    for i, t in enumerate(text):
        if t == '(':
            s.push(i)

        if t == ')':
            value = s.pop()

            if value == inp_in:
                print('correct', i)


text = "Sometimes (((when) I nest)) them (my parentheticals) too much (like this (and this)) they get confusing."
parenthesis_matching(text, 10)
