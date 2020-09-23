"""
240. Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii/

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def searchRow(row, target):
            if not row:
                return False
            if len(row) <= 2:
                return row[0] == target or row[-1] == target
            mid = len(row) // 2
            return searchRow(row[:mid+1], target) if row[mid] >= target else searchRow(row[mid+1:], target)

        for row in matrix:
            if not row or row[0] > target:
                return False
            if row[0] <= target <= row[-1] and searchRow(row, target):
                return True
        return False


x = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 20
print(Solution().searchMatrix(x,target))