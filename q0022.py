"""
22. Generate Parentheses
Medium

https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

from typing import List


class Solution0:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def helper(s, left, right):
            if left == n and right == n:
                ans.append(s)
                return
            if left == right:
                helper(s+'(', left+1, right)
            else:
                if left < n:
                    helper(s + '(', left + 1, right)
                helper(s + ')', left, right + 1)

        helper("", 0, 0)
        return ans


class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def backtrack(curr, l, r):
            if not l and not r:
                curr = "".join(curr)
                res.append(curr)
                return
            if l:
                curr.append("(")
                backtrack(curr, l - 1, r)
                curr.pop()
            if r > l:
                curr.append(")")
                backtrack(curr, l, r - 1)
                curr.pop()

        backtrack([], n, n)

        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def helper(s, left, right):
            if left == n and right == n:
                ans.append(s)
                return
            if left < n:
                helper(s + '(', left + 1, right)
            if left > right:
                helper(s + ')', left, right + 1)

        helper("", 0, 0)
        return ans


n = 3
print(Solution().generateParenthesis(n))
