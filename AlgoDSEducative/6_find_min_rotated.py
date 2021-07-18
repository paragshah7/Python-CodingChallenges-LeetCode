"""
Find minimum element in a rotated sorted array
https://www.educative.io/courses/algorithms-ds-interview/N0NK6kDPrrN
"""
from icecream import ic as print
import time

def find_min_rotated(arr):
    left = 0
    right = len(arr) - 1
    index = -1

    # 1 element in array
    if len(arr) == 1:
        return 0

    # If array is sorted
    if arr[0] < arr[-1]:
        return 0

    # Special binary search logic
    else:
        while left < right:
            mid = (left + right) // 2
            # print(left, right, mid, arr[mid])
            if arr[mid] > arr[left]:
                left = mid + 1
                index = mid
            elif arr[mid] < arr[right]:
                right = mid - 1
                index = mid

    return index


print("Find minimum rotated :", find_min_rotated([30, 40, 50, 10, 20]))
print("Find minimum rotated :", find_min_rotated([70, 10, 20, 30, 40, 50, 60]))
print("Find minimum rotated :", find_min_rotated([0, 1, 2, 3, 4, 5]))
print("Find minimum rotated :", find_min_rotated([0]))
