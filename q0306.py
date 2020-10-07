"""
306. Additive Number
Medium
https://leetcode.com/problems/additive-number/
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.



Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199.
             1 + 99 = 100, 99 + 100 = 199


Constraints:

num consists only of digits '0'-'9'.
1 <= num.length <= 35
Follow up:
How would you handle overflow for very large input integers?
"""


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return False

        def helper(x1, x2, s):
            # check if s is an additive number after x1 and x2
            if not s:
                return True
            if s[0] == '0':
                return not (x1 + x2)
            x3 = str(x1 + x2)
            return len(x3) <= len(s) and s[:len(x3)] == x3 and helper(x2, x1 + x2, s[len(x3):])

        idx1_max = 2 if num[0] == '0' else (n + 1) // 2
        for idx1 in range(1, idx1_max):
            idx2_max = 2 if num[idx1] == '0' else min(n - 2 * idx1, (n - idx1) // 2) + 1
            for idx2 in range(1, idx2_max):
                x1, x2 = int(num[:idx1]), int(num[idx1:idx1 + idx2])
                if helper(x1, x2, num[idx1 + idx2:]):
                    return True
        return False

num = "121474836472147483648"
print(Solution().isAdditiveNumber(num))