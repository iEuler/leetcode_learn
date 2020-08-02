"""
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [
−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer
overflows.

"""


class Solution:
    def reverse(self, x: int) -> int:
        sgn = 1 if x >= 0 else -1
        ans = 0
        x *= sgn

        while x:
            ans = 10*ans + x%10
            x = x // 10
        return 0 if ans > 2**31 - 1 else sgn*ans

x = -120
print(Solution().reverse(x))