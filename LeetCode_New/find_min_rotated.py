"""
Find min in a rotated sorted array

nums = [3,4,5,1,2]
nums = [4,5,6,7,0,1,2]
nums = [11,13,15,17]
"""
import time
from icecream import ic as print

def findMin(nums):
    print(nums)
    left = 0
    right = len(nums) - 1
    min_n = nums[0]

    while left <= right:
        # time.sleep(1)
        mid = (left + right) // 2
        # print(mid, nums[mid])å

        if nums[mid] > nums[left]:
            if nums[left] < min_n:
                min_n = nums[left]
            left = mid + 1
        else:
            if nums[mid] < min_n:
                min_n = nums[mid]
            right = mid - 1

    print(min_n)


findMin([3,4,5,1,2])
findMin([4,5,6,7,0,1,2])
findMin([11,13,15,17])
