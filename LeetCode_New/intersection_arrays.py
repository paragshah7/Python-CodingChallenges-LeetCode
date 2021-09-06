"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""

def intersection_arrays(nums1, nums2):
    num1_dict = {}
    op = []
    for num in nums1:
        num1_dict[num] = 1

    for num in nums2:
        if num in num1_dict and num1_dict[num] == 1:
            op.append(num)
            num1_dict[num] = 0

    print(op)


nums1 = [1,2,2,1]
nums2 = [2,2]
intersection_arrays(nums1, nums2)
