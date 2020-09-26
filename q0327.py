"""
327. Count of Range Sum
Hard
https://leetcode.com/problems/count-of-range-sum/

Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.


Constraints:

0 <= nums.length <= 10^4
"""

from typing import List

from bisect import bisect_left, bisect_right


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        res = 0
        presum = 0
        sorted_presum = []
        for k in range(len(nums)):
            presum += nums[k]
            if lower <= presum <= upper:
                res += 1
            idx_c = bisect_right(sorted_presum, presum)
            idx_l = bisect_left(sorted_presum, presum - upper)
            idx_r = bisect_right(sorted_presum, presum - lower)
            res += idx_r - idx_l

            sorted_presum[idx_c:idx_c] = [presum]

        return res


class Solution0:
    # extended version, return the list of sub intervals
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:

        # ans = []
        res = 0
        presum = 0
        sorted_presum, sorted_idx = [], []
        for k in range(len(nums)):
            presum += nums[k]
            if lower <= presum <= upper:
                # ans.append([0,k])
                res += 1
            idx_c = bisect_right(sorted_presum, presum)
            idx_l = bisect_left(sorted_presum, presum - upper)
            idx_r = bisect_right(sorted_presum, presum - lower)

            for idx in range(idx_l, idx_r):
                # ans.append([sorted_idx[idx]+1, k])
                res += 1

            sorted_presum[idx_c:idx_c] = [presum]
            sorted_idx[idx_c:idx_c] = [k]

        return res

nums = [-2,5,-1]
lower = -2
upper = 2
print(Solution().countRangeSum(nums,lower,upper))

# ==========================

class Solution_test:
    def helper(self, sorted_tuples, target):
        n = len(sorted_tuples)
        if n == 0:
            return 0
        if target >= sorted_tuples[-1][0]:
            return n
        left, right = 0, n - 1
        while right > left + 1:
            mid = (left + right) // 2
            if sorted_tuples[mid][0] > target:
                right = mid
            else:
                left = mid
        return right


x = [(1,3),(5,6),(8,9)]
target = 5

print(Solution_test().helper(x,target))