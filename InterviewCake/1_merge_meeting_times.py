"""
https://www.interviewcake.com/question/python3/merging-ranges?course=fc1&section=array-and-string-manipulation

Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.

For example, given:

  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

Python 3.6
your function would return:

  [(0, 1), (3, 8), (9, 12)]
"""

from icecream import ic as print

def merge_ranges(meet_times):

    # In place sort - .sort() method, original dict is lost
    meet_times.sort()
    print(meet_times)

    meet_ranges = []
    previous_meet = meet_times[0]

    for start, end in meet_times[1:]:

        # Comparing start of current to end of previous meet
        if start <= previous_meet[1]:
            previous_meet = (previous_meet[0], end)
            print(previous_meet)
        else:
            meet_ranges.append(previous_meet)
            previous_meet = (start, end)

    # Appending last meet range
    meet_ranges.append(previous_meet)
    return meet_ranges


ranges = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
print(merge_ranges(ranges))
