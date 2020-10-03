"""
47. Permutations II
Medium
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        path = []

        def backtracking(lst):
            # permutation of lst
            if not lst:
                ans.append(path[:])
            else:
                last = ''
                for k in range(len(lst)):
                    if lst[k] != last:
                        last = lst[k]
                        path.append(lst[k])
                        backtracking(lst[:k] + lst[k + 1:])
                        path.pop()

        backtracking(nums)
        return ans

nums = [1,1,3]
print(Solution().permuteUnique(nums))