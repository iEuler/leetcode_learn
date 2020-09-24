"""
312. Burst Balloons
Hard
https://leetcode.com/problems/burst-balloons/

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""

from typing import List

class Solution1:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [_ for _ in nums if _]
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        memo = {}

        def helper(sub):
            if tuple(sub) in memo:
                return memo[tuple(sub)]
            sub = sub[::-1]
            if tuple(sub) in memo:
                return memo[tuple(sub)]
            if len(sub) == 2:
                return sub[0] * sub[1] + max(sub)

            coins = 0
            for j in range(len(sub)):
                if j == 0:
                    coin = sub[0]*sub[1]
                elif j == len(sub)-1:
                    coin = sub[-2]*sub[-1]
                else:
                    coin = sub[j-1] * sub[j]*sub[j+1]
                coins = max(coins, coin+helper(sub[:j]+sub[j+1:]))

            memo[tuple(sub)] = coins
            return coins

        return helper(nums)


class Solution2:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [_ for _ in nums if _]
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        nums = [1] + nums + [1]

        memo = {}
        # memo[{](i,j)]  means the maximum coins we get after we burst all the balloons between i and j in the original
        # array

        def helper(left, right):
            if right < left:
                return 0
            if (left, right) in memo:
                return memo[(left,right)]

            coins = 0
            for k in range(left, right+1):
                # k-th balloon is the last one to burst
                coins = max(coins, helper(left, k-1) + helper(k+1, right) + nums[left-1]*nums[k]*nums[right+1])

            memo[(left, right)] = coins
            return coins

        return helper(1,len(nums)-2)



class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [_ for _ in nums if _]
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        nums = [1] + nums + [1]

        n = len(nums)

        dp = [[0] * n for _ in range(n)]
        # dp[i][j]  means the maximum coins we get after we burst all the balloons between i and j in the original
        # array

        for size in range(0, n - 2):
            for i in range(1, n - 1 - size):
                left, right = i, i + size
                dp[left][right] = max(
                    dp[left][k - 1] + dp[k + 1][right] + nums[left - 1] * nums[k] * nums[right + 1] for k in
                    range(left, right + 1))

        return dp[1][len(nums) - 2]


x = [3,1,5,8]
print(Solution().maxCoins(x))
