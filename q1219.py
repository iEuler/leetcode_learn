"""
1219. Path with Maximum Gold
Medium
https://leetcode.com/problems/path-with-maximum-gold/
In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position you can walk one step to the left, right, up or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.


Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.


Constraints:

1 <= grid.length, grid[i].length <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.

"""

from typing import List

class Solution:
    max_gold = 0
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        nRow, nCol = len(grid), len(grid[0])
        self.max_gold = max([x for r in grid for x in r])

        path = []

        def helper(kr, kc):
            up = kr == 0 or grid[kr - 1][kc] == 0
            down = kr == nRow - 1 or grid[kr + 1][kc] == 0
            left = kc == 0 or grid[kr][kc - 1] == 0
            right = kc == nCol - 1 or grid[kr][kc + 1] == 0

            if up and down and left and right:
                self.max_gold = max(self.max_gold, sum(path) + grid[kr][kc])
            else:
                path.append(grid[kr][kc])
                grid[kr][kc] = 0
                if not up:
                    helper(kr - 1, kc)
                if not down:
                    helper(kr + 1, kc)
                if not left:
                    helper(kr, kc - 1)
                if not right:
                    helper(kr, kc + 1)
                grid[kr][kc] = path.pop()

        for kr in range(nRow):
            for kc in range(nCol):
                if grid[kr][kc]:
                    helper(kr, kc)

        return self.max_gold

grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
grid = [[0,6,0],[5,8,7],[0,9,0]]
grid = [[0,6,0],[5,8,7],[0,10,0]]
grid = [[34,0,1,0,0,0],[0,0,2,0,1,0],[5,4,3,7,4,2],[0,0,5,0,1,4],[0,0,5,0,2,3]]
print(Solution().getMaximumGold(grid))
# print(Solution().max_gold)