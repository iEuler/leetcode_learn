"""
90. Subsets II
Medium
https://leetcode.com/problems/subsets-ii/
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[], nums]
        path = []
        n = len(nums)

        def backtracking(start, need):
            # choose (need) numbers from [start:n]
            if need == 0:
                ans.append(path[:])
            elif start >= n:
                return
            else:
                last = ''
                for i in range(start, n + 1 - need):
                    if nums[i] != last:
                        last = nums[i]
                        path.append(nums[i])
                        backtracking(i + 1, need - 1)
                        path.pop()

        for k in range(1, n):
            backtracking(0, k)

        return ans

nums = [1,2,2]
print(Solution().subsetsWithDup(nums))