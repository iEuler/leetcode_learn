"""
37. Sudoku Solver
Hard
https://leetcode.com/problems/sudoku-solver/

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.

"""

from typing import List


class Solution0:
    actions = []
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        block2rc = [[] for x in range(9)]
        for k in range(9):
            for m in range(9):
                block2rc[k//3*3+m//3].append((k,m))
        candi = dict() # candi[k,m, block] tracks allowed candidates at location (k,m)
        for k,r in enumerate(board):
            for m,c in enumerate(r):
                if c=='.':
                    cand = [1]*9
                    block = k//3*3+m//3
                    conflist = r + [r2[m] for r2 in board] + [board[bb[0]][bb[1]] for bb in block2rc[block]]
                    for ele in conflist:
                        if ele != '.':
                            cand[int(ele)-1] = 0
                    candi[k,m, block] = cand
        hasOneHot = True
        while hasOneHot:
            hasOneHot = False
            for rc in candi:
                if sum(candi[rc]) == 1:
                    hasOneHot = True
                    number = sum( [candi[rc][k] * (k+1) for k in range(9)] )
                    board[rc[0]][rc[1]] = str(number)
                    self.actions.append([rc[0],rc[1]])
                    for rc2 in candi:
                        if rc2[0] == rc[0] or rc2[1] == rc[1] or rc2[2] == rc[2]:
                            candi[rc2][number-1] = 0
        for rc, ar in list(candi.items()):
            if sum(ar) == 0:
                if board[rc[0]][rc[1]] == '.':
                    return
                else:
                    del candi[rc]
        if ('.' not in [c for r in board for c in r]):
            return
        else:
            minCandi = 10
            for rc in candi:
                if sum(candi[rc]) < minCandi:
                    minCandi = sum(candi[rc])
                    minRC = rc
            for k in range(9):
                if candi[minRC][k] == 1:
                    board[minRC[0]][minRC[1]] = str(k+1)
                    self.actions.append([minRC[0],minRC[1]])
                    revertIndex = len(self.actions)
                    self.solveSudoku(board)
                    if ('.' not in [c for r in board for c in r]):
                        return
                    else:
                        for k in range(len(self.actions)-1, revertIndex-1,-1):
                            board[self.actions[k][0]][self.actions[k][1]] = '.'
                            self.actions.pop()
        return


class Solution:
    # Runtime: 1556 ms, faster than 5.02% of Python3 online submissions for Sudoku Solver.
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # allowed_row = [[] for _ in range(9)]
        # allowed_col = [[] for _ in range(9)]
        # allowed_blk = [[] for _ in range(9)]

        def isAllowed(r, c, ch):
            # check if ch isAllowed at position r,c
            conflicted = set(board[r] + [row[c] for row in board] + [board[r//3*3+x][c//3*3+y] for x in range(3) for y in range(3)])
            return ch not in conflicted

        def backtracking(k):
            if k == 81:
                return True
            r, c = k // 9, k % 9
            if board[r][c] != '.':
                return backtracking(k+1)
            else:
                success = False
                for ch in '123456789':
                    if isAllowed(r, c, ch):
                        board[r][c] = ch
                        success = success or backtracking(k + 1)
                        if not success:
                            board[r][c] = '.'
                        else:
                            break
                return success

        backtracking(0)


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(board)
print(board)