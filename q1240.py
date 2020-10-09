"""
1240. Tiling a Rectangle with the Fewest Squares
Hard
https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/
Given a rectangle of size n x m, find the minimum number of integer-sided squares that tile the rectangle.



Example 1:



Input: n = 2, m = 3
Output: 3
Explanation: 3 squares are necessary to cover the rectangle.
2 (squares of 1x1)
1 (square of 2x2)
Example 2:



Input: n = 5, m = 8
Output: 5
Example 3:



Input: n = 11, m = 13
Output: 6


Constraints:

1 <= n <= 13
1 <= m <= 13
Accepted
7,770
Submissions
15,366
"""


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        memo = {}

        def helper(w, h):
            if w > h:
                w, h = h, w
            # w <= h
            if (w, h) not in memo:
                if w == h:
                    ans = 1
                elif w == 1:
                    ans = h
                elif w == 0:
                    ans = 0
                else:
                    ans = w * h
                    for iw in range(1, w//2+1):  # divide along w
                        ans = min(ans, helper(iw, h) + helper(w - iw, h))
                    for ih in range(1, h//2+1):  # divide along h
                        ans = min(ans, helper(w, ih) + helper(w, h - ih))
                    for iw in range(1, (w + 1) // 2):  # divide out a square in the middle
                        for ih in range(1, (h + 1) // 2):
                            for s in range(1, min(w - 2*iw, h - 2*ih) + 1):
                                ans = min(ans, 1 + helper(iw + s, ih) + helper(w - iw - s, ih + s)
                                          + helper(w - iw, h - ih - s) + helper(iw, h - ih))
                memo[(w, h)] = ans
            return memo[(w, h)]
        return helper(n, m)


n = 11
m = 13
print(Solution().tilingRectangle(n,m))