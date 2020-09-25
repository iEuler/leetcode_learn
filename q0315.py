"""
315. Count of Smaller Numbers After Self
Hard
https://leetcode.com/problems/count-of-smaller-numbers-after-self/

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.


Constraints:

0 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

"""

from typing import List
class Solution1:
    # Time Limit Exceeded
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] *n

        for i in range(1, n):
            for j in range(0, i):
                if nums[j] > nums[i]:
                    ans[j] += 1
        return ans


class Solution2:
    def countSmaller(self, nums):
        def sort(enum):
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller


from bisect import bisect_left
class Solution:
    def countSmaller(self, a):
        n=len(a)
        ans=[0]*n
        seen=[]
        for i in range(n-1,-1,-1):
            idx=bisect_left(seen,a[i])
            ans[i]=idx
            seen[idx:idx]=[a[i]]
        return ans

nums = [5,2,6,1]
print(Solution().countSmaller(nums))