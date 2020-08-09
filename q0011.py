"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

"""

class Solution0:
    def maxArea(self, height: list) -> int:

        n = len(height)
        left, right = [0], [n-1]

        for k in range(1,n):
            if height[k] > height[left[-1]]:
                left.append(k)
        for k in range(n-2,-1,-1):
            if height[k] > height[right[-1]]:
                right.append(k)

        l, r = left.pop(), right.pop()
        ans = (r - l) * height[l]
        while left or right:
            if not left or (right and height[right[-1]] >= height[left[-1]]):
                r = right.pop()
            else:
                l = left.pop()
            ans = max( ans, (r - l) * min(height[l], height[r]) )

        return ans


class Solution:
    def maxArea(self, height: list) -> int:

        n = len(height)
        ans, l, r = 0, 0, n-1
        while l < r:
            if height[l]<height[r]:
                ans = max(ans, (r-l) * height[l])
                l += 1
            else:
                ans = max(ans, (r - l) * height[r])
                r -= 1

        return ans

h = [1,8,6,2,5,4,8,3,7]
h = [2,3,4,5,18,17,6]
print(Solution().maxArea(h))