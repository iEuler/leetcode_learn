"""
200. Number of Islands
Medium
https://leetcode.com/problems/number-of-islands/
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        nRow, nCol = len(grid), len(grid[0])

        def helper(kr, kc):
            grid[kr][kc] = '0'
            kr > 0 and grid[kr - 1][kc] == '1' and helper(kr - 1, kc)
            kr < nRow - 1 and grid[kr + 1][kc] == '1' and helper(kr + 1, kc)
            kc > 0 and grid[kr][kc - 1] == '1' and helper(kr, kc - 1)
            kc < nCol - 1 and grid[kr][kc + 1] == '1' and helper(kr, kc + 1)

        ans = 0
        for kr in range(nRow):
            for kc in range(nCol):
                if grid[kr][kc] == '1':
                    ans += 1
                    helper(kr, kc)

        return ans

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(grid))