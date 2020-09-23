"""
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

"""

from typing import List
from queue import PriorityQueue


class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = PriorityQueue(maxsize=k)
        q.put(-1* float('inf'))
        for num in nums:
            if q.qsize() == k and q.queue[0] < num:
                q.get()
            if q.qsize() < k:
                q.put(num)
            print(q.queue)

        return q.queue[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

k, x = 4, [3,2,3,1,2,4,5,5,6]
k, x = 2, [3,2,1,5,6,4]
print(Solution().findKthLargest(x, k))