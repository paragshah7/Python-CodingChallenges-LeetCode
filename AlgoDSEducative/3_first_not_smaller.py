"""
https://www.educative.io/courses/algorithms-ds-interview/YV6DxN7PyN9
First Element Not Smaller Than Target
"""
from icecream import ic as print

def first_not_smaller(arr, target) -> int:
    left = 0
    right = len(arr) - 1
    if right == 0:
        return 0

    while left <= right:
        mid = (left + right) // 2
        # print(left, right, mid, arr[mid])
        if arr[mid] <= target <= arr[mid + 1]:
            return mid + 1
        elif target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1

    return -1


print("Find first element :",first_not_smaller([1, 3, 3, 5, 8, 8, 10],2))
print("Find first element :",first_not_smaller([0],0))
print("Find first element :",first_not_smaller([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],10))
print("Find first element :",first_not_smaller([1, 1, 1, 1, 4, 5],3))
