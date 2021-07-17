'''
Binary Search
https://www.educative.io/courses/algorithms-ds-interview/JE6qXJ3RWVJ
'''
from icecream import ic as print

def binary_search(arr: list, target: int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        # print(left, right, mid, arr[mid])
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1

    return -1


arr = [10,20,30,40,50,60]
target = 50
print('Binary Search, Index of target -', binary_search(arr, target))
