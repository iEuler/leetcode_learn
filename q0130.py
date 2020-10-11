"""
130. Surrounded Regions
Medium
https://leetcode.com/problems/surrounded-regions/
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Accepted
259,810
Submissions
908,799
"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) <= 2 or len(board[0]) <= 2:
            return

        nRow, nCol = len(board), len(board[0])

        def helper(kr, kc):
            board[kr][kc] = '.'
            kr > 0 and board[kr - 1][kc] == 'O' and helper(kr - 1, kc)
            kr < nRow - 1 and board[kr + 1][kc] == 'O' and helper(kr + 1, kc)
            kc > 0 and board[kr][kc - 1] == 'O' and helper(kr, kc - 1)
            kc < nCol - 1 and board[kr][kc + 1] == 'O' and helper(kr, kc + 1)

        for kr in [0, nRow - 1]:
            for kc in range(nCol):
                if board[kr][kc] == 'O':
                    helper(kr, kc)
        for kc in [0, nCol - 1]:
            for kr in range(nRow):
                if board[kr][kc] == 'O':
                    helper(kr, kc)

        for kr in range(nRow):
            for kc in range(nCol):
                if board[kr][kc] == 'O':
                    board[kr][kc] = 'X'
                elif board[kr][kc] == '.':
                    board[kr][kc] = 'O'

        return

class Solution1:
    nRow, nCol = 0, 0
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) <= 2 or len(board[0]) <= 2:
            return

        self.nRow, self.nCol = len(board), len(board[0])

        def helper(kr, kc):
            board[kr][kc] = '.'
            kr > 0 and board[kr - 1][kc] == 'O' and helper(kr - 1, kc)
            kr < self.nRow - 1 and board[kr + 1][kc] == 'O' and helper(kr + 1, kc)
            kc > 0 and board[kr][kc - 1] == 'O' and helper(kr, kc - 1)
            kc < self.nCol - 1 and board[kr][kc + 1] == 'O' and helper(kr, kc + 1)

        for kr in [0, self.nRow - 1]:
            for kc in range(self.nCol):
                if board[kr][kc] == 'O':
                    helper(kr, kc)
        for kc in [0, self.nCol - 1]:
            for kr in range(self.nRow):
                if board[kr][kc] == 'O':
                    helper(kr, kc)

        for kr in range(self.nRow):
            for kc in range(self.nCol):
                if board[kr][kc] == 'O':
                    board[kr][kc] = 'X'
                elif board[kr][kc] == '.':
                    board[kr][kc] = 'O'

        return

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Solution().solve(board)
for b in board:
    print(b)
