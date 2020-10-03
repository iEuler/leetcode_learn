"""
46. Permutations
Medium
https://leetcode.com/problems/permutations/

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def backtracking(lst):
            # permutation of lst
            if not lst:
                ans.append(path[:])
            else:
                for k in range(len(lst)):
                    path.append(lst[k])
                    backtracking(lst[:k]+lst[k+1:])
                    path.pop()

        backtracking(nums)
        return ans


nums = [1,2,3]
print(Solution().permute(nums))