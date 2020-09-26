"""
493. Reverse Pairs
Hard
https://leetcode.com/problems/reverse-pairs/

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
"""

from typing import List

from bisect import bisect_right
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        sorted_nums = [nums[0]]
        for k in range(1, len(nums)):
            idx2 = bisect_right(sorted_nums, 2*nums[k])
            idx = bisect_right(sorted_nums, nums[k])
            ans += k - idx2
            sorted_nums[idx:idx] = [nums[k]]
        return ans


x = [1,3,2,3,1]
x = [2,4,3,5,1]
print(Solution().reversePairs(x))