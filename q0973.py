"""
973. K Closest Points to Origin
Medium
https://leetcode.com/problems/k-closest-points-to-origin/

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)



Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)


Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""

from typing import List
from bisect import bisect_left

class Solution0:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        sorted_dist = [float('inf')]
        sorted_idx = [-1]
        for k in range(len(points)):
            point = points[k]
            dis = point[0]*point[0]+point[1]*point[1]
            if len(sorted_dist) < K or dis < sorted_dist[-1]:
                idx = bisect_left(sorted_dist, dis)
                sorted_dist[idx:idx] = [dis]
                sorted_idx[idx:idx] = [k]
                if len(sorted_dist)>K:
                    sorted_dist = sorted_dist[:K]
                    sorted_idx = sorted_idx[:K]

        return [points[sorted_idx[k]] for k in range(K)]


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dists = []
        for k in range(len(points)):
            point = points[k]
            dis = point[0]*point[0]+point[1]*point[1]
            dists.append((dis, k))

        dists.sort(key=lambda x: x[0])
        return [points[dists[k][1]] for k in range(K)]


points = [[1,3],[-2,2]]
K = 1
points = [[3, 3], [5, -1], [-2, 4]]
K = 2
print(Solution().kClosest(points, K))