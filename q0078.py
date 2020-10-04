"""
78. Subsets
Medium
https://leetcode.com/problems/subsets/
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
from typing import List

class Solution0:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[], nums]
        path = []
        n = len(nums)

        def backtracking(start, need):
            # choose (need) numbers from [start:n]
            if need == 0:
                ans.append(path[:])
            else:
                for i in range(start, n + 1 - need):
                    path.append(nums[i])
                    backtracking(i + 1, need - 1)
                    path.pop()

        for k in range(1, n):
            backtracking(0, k)

        return ans

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        for i in range(2 << n-1, 2 << n):
            i2bit = bin(i)[3:]
            tmp = []
            for j in range(n):
                if i2bit[j] == '1':
                    tmp.append(nums[j])
            ans.append(tmp)

        return ans



nums = [1, 2, 3]
print(Solution().subsets(nums))