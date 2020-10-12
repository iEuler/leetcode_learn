"""
210. Course Schedule II
Medium
https://leetcode.com/problems/course-schedule-ii/
There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]


Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""

from typing import List
from queue import Queue
class Solution1:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1:
            return [0]
        pres = [[] for k in range(numCourses)]
        follow = {k: [] for k in range(numCourses)}
        for target, pre in prerequisites:
            follow[pre].append(target)
            pres[target].append(pre)

        q = Queue()
        for k in range(numCourses):
            if not pres[k]:
                q.put(k)

        ans = []
        while not q.empty():
            pre = q.get()
            ans.append(pre)
            for target in follow[pre]:
                pres[target].remove(pre)
                if not pres[target]:
                    q.put(target)

        return [] if sum([len(p) for p in pres]) else ans


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1:
            return [0]
        pres = [[] for k in range(numCourses)]
        follow = {k: [] for k in range(numCourses)}
        for target, pre in prerequisites:
            follow[pre].append(target)
            pres[target].append(pre)

        ans = []
        for k in range(numCourses):
            if not pres[k]:
                ans.append(k)

        i = 0
        while i < len(ans):
            pre = ans[i]
            for target in follow[pre]:
                pres[target].remove(pre)
                if not pres[target]:
                    ans.append(target)
            i += 1

        return ans if len(ans) == numCourses else []

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(Solution().findOrder(numCourses,prerequisites))