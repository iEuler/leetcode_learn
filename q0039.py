"""
39. Combination Sum
Medium
https://leetcode.com/problems/combination-sum/

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]


Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
Each element of candidate is unique.
1 <= target <= 500
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        memo = {}
        min_num = min(candidates)

        def backtracking(t):
            if t == 0:
                return [[0]]
            if t < min_num:
                return []
            if t not in memo:
                paths = []
                for num in candidates:
                    if num <= t:
                        subpaths = backtracking(t-num)
                        for path in subpaths:
                            x = sorted([num] + path)
                            if x not in paths:
                                paths.append(x)
                memo[t] = paths
            return memo[t]

        backtracking(target)
        return [x[1:] for x in memo[target]] if memo else []


# candidates = [2,3,6,7]
# target = 7
candidates = [2,3,5]
target = 8
print(Solution().combinationSum(candidates, target))