"""
52. N-Queens II
Hard
https://leetcode.com/problems/n-queens-ii/

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


class Solution0:
    def totalNQueens(self, n: int) -> int:
        path = [0]*n
        half = (n+1) // 2
        ans = []

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
                ans.append(1)
                if path[0] != n // 2:
                    ans.append(1)
            else:
                for col in range(n):
                    if isAllowed(row, col):
                        path[row] = col
                        backtracking(row+1)

        backtracking(0)

        return len(ans)


class Solution:
    # same idea, just accelerate the isAllow function.
    def totalNQueens(self, n: int) -> int:
        row_mask, col_mask, pos_dig, neg_dig = [False]*n, [False]*n, [False]*(2*n-1), [False]*(2*n-1)
        def helper(row):
            if row == n:
                return 1
            cnt = 0
            row_mask[row] = True
            for col in range(n):
                if not col_mask[col] and not pos_dig[row + n - col -1] and not neg_dig[row + col]:
                    col_mask[col] = True
                    pos_dig[row + n - col - 1] = True
                    neg_dig[row + col] = True
                    cnt += helper(row+1)
                    col_mask[col] = False
                    pos_dig[row + n - col - 1] = False
                    neg_dig[row + col] = False
            return cnt
        return helper(0)

n = 8
print(Solution().totalNQueens(n))