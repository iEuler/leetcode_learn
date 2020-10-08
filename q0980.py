"""
980. Unique Paths III
Hard
https://leetcode.com/problems/unique-paths-iii/

On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.



Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation:
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.


Note:

1 <= grid.length * grid[0].length <= 20
"""

from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        memo = {}
        nRow, nCol = len(grid), len(grid[0])
        nZero = 0
        for kr, r in enumerate(grid):
            for kc, c in enumerate(r):
                if c == 0:
                    nZero += 1
                elif c == 1:
                    start = (kr,kc)
                elif c == 2:
                    terminal = (kr,kc)
        grid[start[0]][start[1]] = 0
        nZero += 1

        g0 = tuple([c for r in grid for c in r])

        def helper(g, cur, n):
            if (g, cur) not in memo:
                if n == 1:
                    # if abs(terminal[0] - cur[0]) + abs(terminal[1] - cur[1]) == 1:
                    #     print('a', terminal,cur)
                    # if bool(terminal[0] - cur[0] in (-1,1)) != bool(terminal[1] - cur[1] in (-1,1)):
                    #     print('b', terminal, cur)
                    # return 1 if abs(terminal[0] - cur[0]) + abs(terminal[1] - cur[1]) == 1 else 0
                    # return 1 if bool(terminal[0] - cur[0] in (-1,1)) != bool(terminal[1] - cur[1] in (-1,1)) else 0
                    return 1 if (terminal[0] - cur[0], terminal[1] - cur[1]) in (
                    (0, 1), (0, -1), (1, 0), (-1, 0)) else 0


                ans = 0
                grid[cur[0]][cur[1]] = -1  # mark next location
                g_nxt = tuple([c for r in grid for c in r])
                if cur[1] < nCol - 1 and grid[cur[0]][cur[1] + 1] == 0:
                    ans += helper(g_nxt, (cur[0], cur[1] + 1), n - 1)
                if cur[0] < nRow - 1 and grid[cur[0] + 1][cur[1]] == 0:
                    ans += helper(g_nxt, (cur[0] + 1, cur[1]), n - 1)
                if cur[1] > 0 and grid[cur[0]][cur[1] - 1] == 0:
                    ans += helper(g_nxt, (cur[0], cur[1] - 1), n - 1)
                if cur[0] > 0 and grid[cur[0] - 1][cur[1]] == 0:
                    ans += helper(g_nxt, (cur[0] - 1, cur[1]), n - 1)
                grid[cur[0]][cur[1]] = 0  # mark next location

                memo[(g, cur)] = ans
            return memo[(g,cur)]

        return helper(g0, start, nZero)

grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# grid = [[1,0,0],[2,0,0]]
print(Solution().uniquePathsIII(grid))