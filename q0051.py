"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans_num = []
        path = [0]*n
        half = (n+1) // 2

        def isAllowed(row, col):
            if row == 0 and col >= half:
                return False
            if row == 1 and path[0] == n // 2 and col > n // 2:
                return False
            for r in range(row):
                if col == path[r] or col == path[r] + (row  - r) or col == path[r] - (row - r):
                    return False
            return True

        def backtracking(row):
            if row == n:
                ans_num.append(path[:])
                if path[0] != n // 2:
                    ans_num.append([n-1-k for k in path])
            else:
                for col in range(n):
                    if isAllowed(row, col):
                        path[row] = col
                        backtracking(row+1)

        backtracking(0)
        ans = []
        for a in ans_num:
            path = []
            for k in a:
                path.append('.'*k + 'Q' + '.'*(n-k-1))
            ans.append(path)
        return ans_num

n = 5
print(Solution().solveNQueens(n))