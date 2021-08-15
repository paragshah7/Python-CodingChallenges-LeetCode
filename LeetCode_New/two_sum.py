"""
Two Sum
https://leetcode.com/problems/two-sum/

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1]

Sol: O(n) + O(n) space
loop through if diff not in dict key, add to dict, else return dict value and index
or

Use dict - O(n)
for loop and look up diff from dict key
"""

def two_sum(nums, target):

    num_dict = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in num_dict:
            return num_dict[diff], index
        num_dict[num] = index

    # for index, num in enumerate(nums):
    #     diff = target - num
    #     if diff in num_dict:
    #         return index, num_dict[diff]


nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))
