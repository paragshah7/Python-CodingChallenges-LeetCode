"""
https://www.interviewcake.com/question/python3/find-rotation-point?course=fc1&section=sorting-searching-logarithms
"""


# def find_rotation_point(words):
#     first = 0
#     last = len(words) - 1
#
#     while first < last:
#         middle = first + (last - first) // 2
#
#         if words[middle] >= words[first]:
#             # Go below
#             first = middle
#         else:
#             # Go above
#             last = middle
#
#         if first + 1 == last:  # please remember this condition, its the most important statement of this program
#             return last

from icecream import ic as print

def find_rotation_point(words):
    left = 0
    right = len(words) - 1
    mid = (left + right) // 2

    while left <= right:
        mid = (left + right) // 2
        # print(left, right, mid)

        if words[left] <= words[mid]:
            left = mid + 1
            if words[mid] > words[left]:
                return mid+1
        else:
            right = mid - 1
            if words[mid] < words[right]:
                return mid


words = [
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
    'karpatka',

]

print(find_rotation_point(words))
