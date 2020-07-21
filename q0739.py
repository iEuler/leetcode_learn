"""
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

"""

class Solution:
    def dailyTemperatures(self, T: list) -> list:
        q = [0]
        n = len(T)
        ans = [0]*n

        for i in range(1,n):
            while q and T[q[-1]]<T[i]:
                j = q.pop()
                ans[j] = i - j
            q.append(i)

        return  ans


T = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(T))