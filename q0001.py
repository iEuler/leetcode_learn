"""
1. Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        nums2 = sorted([(nums[k],k) for k in range(len(nums))], key= lambda x: x[0])
        left, right = 0, len(nums)-1
        last_sign = 1
        while left < right:
            cur_sum = nums2[left][0] + nums2[right][0]
            if cur_sum == target:
                return [nums2[left][1], nums2[right][1]]
            elif (cur_sum - target)*last_sign < 0:
                left += 1
            elif cur_sum > target:
                right -= 1
                last_sign = 1
            else:
                right += 1
                last_sign = -1


class Solution2:
    def twoSum(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]


nums = [2, 7, 11, 15]
target = 9
nums = [3,2,3]
target = 6
print(Solution().twoSum(nums, target))