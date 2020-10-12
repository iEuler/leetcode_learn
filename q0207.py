"""
207. Course Schedule
Medium
https://leetcode.com/problems/course-schedule/
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
Accepted
474,135
Submissions
1,088,083
"""

from typing import List

class Solution1:
    # use a dfs method
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 1:
            return True
        canLearn = [1] * (numCourses+1)
        pres ={}
        for target, pre in prerequisites:
            if target not in pres:
                pres[target] = []
                canLearn[target] = 0
            pres[target].append(pre)
        pres[numCourses] = [k for k in range(numCourses)]
        canLearn[numCourses] = 0

        path = []
        def helper(k):
            # check if course k can be learned
            if canLearn[k]:
                return True
            if k in path:
                return False
            path.append(k)
            for i in pres[k]:
                if not helper(i):
                    return False
            path.pop()
            canLearn[k] = 1
            return True

        return helper(numCourses)


from queue import Queue
class Solution:
    # use a bfs method
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 1:
            return True
        numPres = [0] * (numCourses)
        follow = {k: [] for k in range(numCourses)}
        for target, pre in prerequisites:
            follow[pre].append(target)
            numPres[target] += 1

        q = Queue()
        for k in range(numCourses):
            if numPres[k] == 0:
                q.put(k)

        while not q.empty():
            pre = q.get()
            for target in follow[pre]:
                numPres[target] -= 1
                if numPres[target] == 0:
                    q.put(target)

        return sum(numPres) == 0


numCourses = 3
prerequisites = [[1,0]]
print(Solution().canFinish(numCourses, prerequisites))