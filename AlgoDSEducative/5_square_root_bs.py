"""
Square root using binary search
https://www.educative.io/courses/algorithms-ds-interview/YV3ElMP53yM
"""
from icecream import ic as print
import time

def square_root(n):
    if n == 0:
        return 0
    left, right = 1, n
    res = -1
    while left <= right:
        mid = (left + right) // 2
        # print(left, right, mid, n)
        if mid * mid <= n:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res


print("Square root:", square_root(4))
print("Square root:", square_root(8))
print("Square root:", square_root(10))
