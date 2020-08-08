"""
10. Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/


Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


class Solution0:
    # This solution is wrong. It actually solves the following question
    # '.' Matches one of the preceding element.
    # '*' Matches zero or more of the preceding element.
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return True if not s else False
        k1, n1, n2 = 0, len(s), len(p)
        k2 = 0
        while k2 < n2 and p[k2] == '*':
            k2 += 1

        while k1 < n1 and k2 < n2:
            if k2 + 1 < n2 and p[k2 + 1] == '*':
                while k2 < n2 and p[k2] == '*':
                    k2 += 1
                k1, k2 = k1 + 1, k2 + 2
                p_last, count = p[k2 - 1], 0
                k2 += 1
                while k2 < n2 and p[k2] in '*.' + p_last:
                    if p[k2] == p_last or (p[k2] == '.' and dot == p_last):
                        count += 1
                    if p[k2] != '.':
                        dot = p[k2]
                    k2 += 1
                while s[k1] == p_last:
                    k1, count = k1 + 1, count - 1
                if count > 0:
                    return False

            if p[k2] in s[k1]+'.':
                k1, k2 = k1+1, k2+1
            elif k2+1 < n2 and p[k2+1] == '*':
                k1, k2 = k1+1, k2+2
                while k2 < n2 and p[k2] == '*':
                    k2 += 1
                k1, k2 = k1 + 1, k2 + 2
                p_last, count = p[k2-1], 0
                k2 += 1
                while k2 < n2 and p[k2] in '*.'+p_last:
                    if p[k2] == p_last or (p[k2] == '.' and dot == p_last):
                        count += 1
                    if p[k2] != '.':
                        dot = p[k2]
                    k2 += 1
                while s[k1] == p_last:
                    k1, count = k1 + 1, count - 1
                if count > 0:
                    return False
            else:
                return False

        return True


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j+1 < len(p) and p[j+1] == '*':
                        ans = dp(i, j+2) or (first_match and dp(i+1, j))
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)




s = "mississippi"
p = "mis*is*p*."
s = "aab"
p = "c*a*b"
s = "aaa"
p = "a*a"
print(Solution1().isMatch(s, p))
