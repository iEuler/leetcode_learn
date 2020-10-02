"""
40. Combination Sum II
Medium
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

from typing import List

class Solution_fail:
    # not working yet
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        memo = {}

        def isSublist(sub, lst):
            # test if sub is a sublist of lst. both sub and lst are sorted
            if len(sub) > len(lst):
                return False
            if sub == lst:
                return True
            i, j = 0, 0
            while i < len(sub) and j < len(lst):
                if sub[i] < lst[j]:
                    return False
                elif sub[i] == lst[j]:
                    i, j = i+1, j+1
                else:
                    j += 1
            return i == len(sub)

        def helper(sub, target):
            # return combinations in sub where the sub numbers sums to target. Here sub is a subset of candidates.
            if target == 0:
                return [[0]]
            if not sub or target < sub[0]:
                return []

        return [[]]


class Solution_test():
    def isSublist(self, sub, lst):
        # test if sub is a sublist of lst
        if len(sub) > len(lst):
            return False
        if sub == lst:
            return True
        i, j = 0, 0
        while i < len(sub) and j < len(lst):
            if sub[i] < lst[j]:
                return False
            elif sub[i] == lst[j]:
                i, j = i + 1, j + 1
            else:
                j += 1
        return i == len(sub)

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def helper(k, t):
            # returns List[List[int]] where sum(List) == t, with List from candidates[k:]
            if k == len(candidates):
                return []
            if candidates[k] == t:
                return [[candidates[k]]]
            elif candidates[k] > t:
                return []
            else:
                ans = []
                for lst in helper(k + 1, t - candidates[k]):
                    ans.append([candidates[k]] + lst)
                j = k + 1
                while j < len(candidates) and candidates[j] == candidates[k]:
                    j += 1
                return ans + helper(j, t)

        return helper(0, target)


candidates = [10,1,2,7,6,1,5]
target = 8
print(Solution().combinationSum2(candidates,target))

# x = [1,2]
# y = [1,1,2,3]
# print(Solution_test().isSublist(x,y))