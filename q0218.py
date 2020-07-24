"""
218. The Skyline Problem
https://leetcode.com/problems/the-skyline-problem/

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

Buildings Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
"""

# NOT ACCEPTED BY LEETCODE YET

from collections import deque


class Solution:
    def getSkyline(self, buildings: list) -> list:
        ans = []
        right = deque()  # list of index of buildings with right end in skyline

        for i,b in enumerate(buildings):

            while right and right[0][0] <= b[0]:
                r = right.popleft()
                if r[0] <= b[0] and r[1] >= r[2]:
                    ans.append([r[0], r[2]])

            ans.append([b[0], b[2]])
            for r in right:
                if r[1] >= b[2]:
                    ans.pop()
                    break

            while len(ans) >= 2 and (ans[-1][0] == ans[-2][0]):
                h = ans.pop()[1]
                ans[-1][1] = max(ans[-1][1], h)
            while len(ans) >= 2 and (ans[-1][1] == ans[-2][1]):
                ans.pop()

            k, right_height = i+1, 0
            while k < len(buildings) and buildings[k][0] <= b[1]:
                if b[1] < buildings[k][1]:
                    right_height = max(right_height, buildings[k][2])
                k += 1

            k, keep = len(right)-1, True
            while k >= 0 and right[k][0] >= b[1]:
                if right[k][1] >= b[2]:
                    keep = False
                    break
                right_height = max(right_height, right[k][1]) if right[k][0] > b[1] else right_height
                k -= 1
            if keep:
                right.insert(k + 1, [b[1], b[2], right_height])

        print(right)
        while right:
            r = right.popleft()
            if r[0] != ans[-1][0] and r[2] != ans[-1][1]:
                ans.append([r[0], r[2]])

        return ans


A = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
# A = [[0,2,3],[2,5,3]]
A = [[1,2,1],[1,2,2],[1,2,3]]
# A = [[0,3,3],[1,5,3],[2,4,3],[3,7,3]]
# A = [[3,10,20],[3,9,19],[3,8,18],[3,7,17],[3,6,16],[3,5,15],[3,4,14]]
# A = [[1,5,3], [1,5,3], [1,5,3]]
# A = [[1,4,1], [2,3,2]]
A = [[1,10001,10000],[2,10001,9999],[3,10001,9998]]
print(Solution().getSkyline(A))

