"""
Peak of mountain array

"""
from icecream import ic as print
import time

def peak_of_mountain_array(arr):
    left = 0
    right = len(arr) - 1
    index = 1
    if len(arr) == 1:
        return 0

    while left <= right:
        mid = (left + right) // 2
        # print(left, right, mid, arr[mid])

        if arr[mid] >= arr[mid+1]:
            index = mid
            right = mid - 1
        else:
            left = mid + 1

    return index


# print("Find Peak of mountain :", peak_of_mountain_array([0, 1, 2, 3, 2, 1, 0]))
print("Find Peak of mountain :", peak_of_mountain_array([0, 10, 3, 2, 1, 2]))
# print("Find Peak of mountain :", peak_of_mountain_array([0, 10, 0]))
