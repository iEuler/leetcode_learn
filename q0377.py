"""
377. Combination Sum IV
Medium
https://leetcode.com/problems/combination-sum-iv/

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.


Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""

from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        memo = {}
        nums.sort()
        min_num = min(nums)

        def backtracking(t):
            if t == 0:
                memo[t] = 1
            elif t < min_num:
                memo[t] = 0
            elif t not in memo:
                path_num = 0
                for num in nums:
                    if num <= t:
                        path_num += backtracking(t - num)
                memo[t] = path_num
            return memo[t]

        backtracking(target)
        return memo[target]

# nums = [1, 2, 3]
# target = 4
nums = [9]
target = 3
print(Solution().combinationSum4(nums, target))