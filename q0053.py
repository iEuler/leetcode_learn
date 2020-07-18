"""
53. Maximum Subarray

https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and
return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is
more subtle.

"""


class Solution:
    # Sliding Window
    def maxSubArray(self, nums: list) -> int:
        """
        :param nums: list[int]
        :return: int
        """

        max_sum = max(nums)
        if max_sum <= 0:
            return max_sum

        left = 0
        while nums[left] <= 0:
            left += 1
        right, now_sum = left + 1, nums[left]
        while right < len(nums):
            now_sum += nums[right]
            if nums[right] >= 0:
                max_sum = max(max_sum, now_sum)
            if now_sum <= 0:
                return max(max_sum, self.maxSubArray(nums[right:]))
            right += 1

        return max_sum


class Solution2:
    # Sliding Window
    def maxSubArray(self, nums: list) -> int:
        """
        :param nums: list[int]
        :return: int
        """

        max_sum, now_sum = -1 * float('inf'), 0
        for num in nums:
            now_sum += num
            max_sum = max(max_sum, num, now_sum)
            if now_sum < 0:
                now_sum = 0

        return max_sum

x = [1, 2, 3, 4]
x = [-2,1,-3,4,-1,2,1,-5,4]
x = [-3,1,-2,2]
print(Solution().maxSubArray.__annotations__)
print(Solution().maxSubArray(x))