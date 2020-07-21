"""
239. Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""


class Solution():
    def maxSlidingWindow(self, nums:list, k:int) -> list:
        if k == 1:
            return nums

        n = len(nums)
        max_list = [0]*n

        max_list[k-1] = nums[k-1]
        for i in range(k-2,-1,-1):
            max_list[i] = max(nums[i], max_list[i+1])

        for i in range(k, n):

            start, end = i-k+1, i-1
            while start < end:
                j = (start+end)//2
                if max_list[j]>=nums[i]:
                    start = j+1
                else:
                    end = j
            start = start+1 if max_list[start]>nums[i] else start

            for j in range(start, i+1):
                max_list[j] = nums[i]

        return max_list[:n-k+1]


class Solution1:
    def maxSlidingWindow(self, nums: list, k: int) -> list:

        if k == 1:
            return nums
        n = len(nums)
        kmax = max(nums[:k])
        res = [kmax]
        for i in range(k, n):
            if kmax <= nums[i]:
                kmax = nums[i]
            elif nums[i - k] == kmax:
                kmax = max(nums[i - k + 1:i + 1])
            res.append(kmax)
        return res



A = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution1().maxSlidingWindow(A,k))