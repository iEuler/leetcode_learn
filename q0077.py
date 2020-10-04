"""
77. Combinations
Medium
https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]


Constraints:

1 <= n <= 20
1 <= k <= n
"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def backtracking(start, need):
            # choose (need) numbers from [start:n]
            if need == 0:
                ans.append(path[:])
            else:
                for num in range(start, n + 1 - need):
                    path.append(num + 1)
                    backtracking(num + 1, need - 1)
                    path.pop()

        backtracking(0, k)

        return ans

n = 4
k = 2
print(Solution().combine(n, k))