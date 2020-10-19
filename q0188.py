"""
188. Best Time to Buy and Sell Stock IV
Hard
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Notice that you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


Constraints:

0 <= k <= 109
0 <= prices.length <= 104
0 <= prices[i] <= 1000
Accepted
149,068
Submissions
522,576
"""

from typing import List


class Solution0:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        def helper(d, k, hold):
            # suppose it's d-th day, and there are k transactions left, and (hold = True/False) indicates we are
            # holding the stock or not
            if k == 0:
                return 0
            if d == len(prices) - 1:
                return prices[d] * hold
            if hold:
                return max(prices[d] + helper(d + 1, k - 1, 0), helper(d + 1, k, 1))
            else:
                return max(-prices[d] + helper(d + 1, k, 1), helper(d + 1, k, 0))

        return helper(0, k, 0) if prices else 0


class Solution1:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n, ret, v, p = len(prices), 0, 0, 0
        profits, vp_pairs = [], []
        while p < n:
            v = p
            while v < n - 1 and prices[v] >= prices[v + 1]: v += 1
            p = v + 1
            while p < n and prices[p] >= prices[p - 1]: p += 1

            while (vp_pairs and prices[v] < prices[vp_pairs[-1][0]]):
                temp = vp_pairs.pop()
                profits.append(prices[temp[1] - 1] - prices[temp[0]])

            while (vp_pairs and prices[p - 1] >= prices[vp_pairs[-1][1] - 1]):
                profits.append(prices[vp_pairs[-1][1] - 1] - prices[v])
                v = vp_pairs.pop()[0]
            vp_pairs.append((v, p))

        while vp_pairs:
            temp = vp_pairs.pop()
            profits.append(prices[temp[1] - 1] - prices[temp[0]])

        k = min(k, len(profits))
        profits.sort(key=lambda x: -x)
        for i in range(k):
            ret += profits[i]
        return ret


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if 2 * k >= len(prices):
            return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))

        pnl = [0] * len(prices)
        for _ in range(k):
            val = 0
            for i in range(1, len(pnl)):
                val = max(pnl[i], val + prices[i] - prices[i - 1])
                pnl[i] = max(pnl[i - 1], val)
        return pnl[-1]
k = 2
prices = [3,2,6,5,0,3]  #[2,4,1]
print(Solution().maxProfit(k, prices))