from typing import List


class Solution:
    def missing_number(self, nums: List[int]) -> int:
        if nums[0] == 1:
            return 0
        if len(nums) == 1:
            return nums[0]+1
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1] != nums[i] + 1:
                return nums[i]+1


obj = Solution()
print(obj.missing_number([9, 6, 4, 2, 3, 8, 7, 0, 1]))
