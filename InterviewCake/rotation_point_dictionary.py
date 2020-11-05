"""
https://www.interviewcake.com/question/python3/find-rotation-point?course=fc1&section=sorting-searching-logarithms
"""


def find_rotation_point(words):
    first = 0
    last = len(words) - 1

    while first < last:
        middle = first + (last - first) // 2

        if words[middle] >= words[first]:
            # Go below
            first = middle
        else:
            # Go above
            last = middle

        if first + 1 == last:  # please remember this condition, its the most important statement of this program
            return last


words = [
    'karpatka',
    'othellolagkage',
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',

]
print(find_rotation_point(words))
