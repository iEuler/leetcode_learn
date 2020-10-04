"""
79. Word Search
Medium
https://leetcode.com/problems/word-search/
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

"""

from typing import List


class Solution0:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return not str
        nRow = len(board)
        nCol = len(board[0])
        used = []
        def backtracking(row, col, k):
            # start from position (row, col), looking for k-th letter in word
            if k == len(word):
                return True
            for (i, j) in [(row + r, col + c) for (r, c) in [(0, 1), (0, -1), (1, 0), (-1, 0)]]:
                if 0 <= i < nRow and 0 <= j < nCol and board[i][j] == word[k] and (i, j) not in used:
                    used.append((i, j))
                    if backtracking(i, j, k+1):
                        return True
                    used.pop()
            return False

        for i in range(nRow):
            for j in range(nCol):
                if board[i][j] == word[0]:
                    used.append((i, j))
                    if backtracking(i, j, 1):
                        return True
                    used.pop()
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # pre check
        if not board or not board[0]:
            return not str
        nRow = len(board)
        nCol = len(board[0])

        if len(word) > nRow * nCol:
            return False
        cnt_board, cnt_word = {}, {}
        for i in range(nRow):
            for j in range(nCol):
                if board[i][j] not in cnt_board:
                    cnt_board[board[i][j]] = 1
                else:
                    cnt_board[board[i][j]] += 1
        for i in range(len(word)):
            if word[i] not in cnt_word:
                cnt_word[word[i]] = 1
            else:
                cnt_word[word[i]] += 1
        for ch in cnt_word.keys():
            if ch not in cnt_board or cnt_word[ch] > cnt_board[ch]:
                return False

        # start recursion
        used = []
        def backtracking(row, col, k):
            # start from position (row, col), looking for k-th letter in word
            if k == len(word):
                return True
            for (i, j) in [(row + r, col + c) for (r, c) in [(0, 1), (0, -1), (1, 0), (-1, 0)]]:
                if 0 <= i < nRow and 0 <= j < nCol and board[i][j] == word[k] and (i, j) not in used:
                    used.append((i, j))
                    if backtracking(i, j, k+1):
                        return True
                    used.pop()
            return False

        for i in range(nRow):
            for j in range(nCol):
                if board[i][j] == word[0]:
                    used.append((i, j))
                    if backtracking(i, j, 1):
                        return True
                    used.pop()
        return False


board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
    ]
word = "ABCCED"
print(Solution().exist(board,word))
