"""
4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""


class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        n = len(nums1)
        m = len(nums2)
        mid = (n + m) // 2

        def helper(left1, left2, k):
            if left1 >= len(nums1):
                return nums2[left2 + k - 1]
            if left2 >= len(nums2):
                return nums1[left1 + k - 1]
            if k == 1:
                return min(nums1[left1], nums2[left2])

            mid1 = left1 + k // 2 - 1
            mid2 = left2 + k // 2 - 1

            val1 = float('inf') if mid1 >= len(nums1) else nums1[mid1]
            val2 = float('inf') if mid2 >= len(nums2) else nums2[mid2]

            if val1 <= val2:
                return helper(mid1 + 1, left2, k - k // 2)
            else:
                return helper(left1, mid2 + 1, k - k // 2)

        if (n + m) % 2 == 0:
            return (helper(0, 0, mid) + helper(0, 0, mid + 1)) / 2
        else:
            return helper(0, 0, mid + 1)

