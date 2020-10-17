"""
279. Perfect Squares
Medium
https://leetcode.com/problems/perfect-squares/
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

# Best solution is to use Lagrange's Four Square Theorem. The answer is from [1,2,3,4].

from queue import Queue
from math import sqrt
class Solution0:
    # dfs
    def numSquares(self, n: int) -> int:
        memo = {j*j: 1 for j in range(int(sqrt(n))+1)}

        squares = [j*j for j in range(int(sqrt(n))+1)]

        def helper(k):
            if k not in memo:
                ans = n
                for x in squares[int(sqrt(k)):0:-1]:
                    ans = min(ans, helper(k - x) + 1)
                memo[k] = ans
            return memo[k]

        return helper(n)


class Solution:
    # bfs
    def numSquares(self, n: int) -> int:

        squares = [j*j for j in range(int(sqrt(n))+1)]
        q = Queue()
        q.put(n)
        level = 0

        while q:
            levelsize = q.qsize()
            level += 1
            for k in range(levelsize):
                k = q.get()
                for x in squares[int(sqrt(k)):0:-1]:
                    if k - x == 0:
                        return level
                    q.put(k-x)


n = 12
print(Solution().numSquares(n))