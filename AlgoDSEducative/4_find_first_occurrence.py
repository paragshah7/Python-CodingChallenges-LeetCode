"""
Find first occurrence of target in a sorted array
https://www.educative.io/courses/algorithms-ds-interview/myz66YL3yYE
"""

from icecream import ic as print
import time

def find_first_occurrence(arr, target) -> int:
    left = 0
    right = len(arr) - 1
    if target == arr[0]:
        return 0

    while left <= right:
        time.sleep(1)
        mid = (left + right) // 2
        # print(left, right, mid, arr[mid])
        if target <= arr[mid]:
            if target == arr[mid] and target > arr[mid-1]:
                return mid
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1

    return -1


print("First occurance :",find_first_occurrence([1, 3, 3, 3, 3, 6, 10, 10, 10, 100], 3))
print("First occurance :",find_first_occurrence([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1))
print("First occurance :",find_first_occurrence([1, 22, 22, 33, 50, 100, 20000], 33))
print("First occurance :",find_first_occurrence([4, 6, 7, 7, 7, 20], 8))
print("First occurance :",find_first_occurrence([6, 7, 9, 10, 10, 10, 90], 10))
print("First occurance :",find_first_occurrence([4], 4))