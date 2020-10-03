"""
44. Wildcard Matching
Hard
https://leetcode.com/problems/wildcard-matching/

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false

"""


class Solution0:
    # run time 1052ms
    def isMatch(self, s: str, p: str) -> bool:
        ns, np = len(s), len(p)
        j = 0
        if np > 0:
            while p[np - 1 - j] == '*' and j < np:
                j += 1
            p = p[:np-j+1] if j else p
            np = len(p)
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == np - 1 and p[j] == '*':
                    ans = True
                elif i == ns or j == np:
                    ans = i+j == ns+np
                elif p[j] == '*':
                    ans = dp(i+1, j) or dp(i, j+1)
                else:
                    ans = (p[j] in (s[i], '?')) and dp(i+1, j+1)
                memo[(i, j)] = ans
            return memo[(i, j)]

        return dp(0,0)


class Solution1:
    # run time 52ms
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ks, kp, star = 0, 0, -1
        while ks < len(s):
            if kp < len(p) and (p[kp] == s[ks] or p[kp] == "?"):
                ks, kp = ks+1, kp+1
            elif kp < len(p) and p[kp] == "*":
                star, kp, ks0 = kp, kp+1, ks
            elif star != -1:
                kp, ks, ks0 = star + 1, ks0+1, ks0+1
            else:
                return False
        while kp < len(p) and p[kp] == "*":
            kp+=1
        return kp == len(p)


class Solution1b:
    # run time 52ms
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ks, kp, star = 0, 0, -1
        while ks < len(s):
            if kp < len(p) and (p[kp] == s[ks] or p[kp] == "?"):
                ks, kp = ks+1, kp+1
            elif kp < len(p) and p[kp] == "*":
                star, kp = kp, kp+1
            elif star != -1:
                kp, ks = star + 1, ks+1
            else:
                return False
        while kp < len(p) and p[kp] == "*":
            kp += 1
        return kp == len(p)

class Solution0b:
    # run time 652ms
    def isMatch(self, s: str, p: str) -> bool:
        temp = ['']
        for ch in p:
            if temp[-1] != '*' or ch != '*':
                temp.append(ch)
        p = ''.join(temp)
        ns, np = len(s), len(p)

        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if i == ns:
                    ans = i+j == ns+np
                elif p[j] == '*':
                    ans = dp(i+1, j) or dp(i, j+1)
                else:
                    ans = (p[j] in (s[i], '?')) and dp(i+1, j+1)
                memo[(i, j)] = ans
            return memo[(i, j)]

        return dp(0,0)

class Solution0b:
    # exceed time limit
    def isMatch(self, s: str, p: str) -> bool:
        temp = ['']
        for ch in p:
            if temp[-1] != '*' or ch != '*':
                temp.append(ch)
        p = ''.join(temp)
        ns, np = len(s), len(p)

        def dp(i, j):
            print(i,j)
            if j == np - 1 and p[j] == '*':
                return True
            elif i == ns or j == np:
                return i+j == ns+np
            elif p[j] == '*':
                return dp(i+1, j) or dp(i, j+1)
            else:
                return (p[j] in (s[i], '?')) and dp(i+1, j+1)

        return dp(0,0)

class Solution:
    # to check if each element of p.split('*') can be found in s without overlap
    def isMatch(self, s: str, p: str) -> bool:
        def isMatch_sub(s, p):
            # check if s = p. p could contain '?'. s and p has same length.
            for (cs, cp) in zip(s,p):
                if cp != cs and cp != '?':
                    return False
            return True

        if not p:
            return not s
        p_list = p.split('*')
        if len(p_list) == 1:
            return len(s) == len(p) and isMatch_sub(s,p)
        p_head, p_tail = p_list[0], p_list[-1]
        left, right = len(p_head), len(s) - len(p_tail)
        if left > right or not isMatch_sub(s[:left], p_head) or not isMatch_sub(s[right:], p_tail):
            return False
        j = left
        for p_sub in p_list[1:-1]:
            while j <= right - len(p_sub) and not isMatch_sub(s[j:j+len(p_sub)], p_sub):
                j += 1
            if j > right - len(p_sub):
                return False
            else:
                j += len(p_sub)
        return True



s = "acdcb"
p = "a*c?b"
# s = "aa"
# p = "*"
s = "agd"
p = "*ab*b**c**"
s = "aaaa"
p = "***a"
s = "abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb"
p = "***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**"

s = "adceb"
p = "*a*b"
s = "c"
p = "*?*"

print(Solution().isMatch(s,p))