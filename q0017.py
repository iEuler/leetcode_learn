"""
17. Letter Combinations of a Phone Number
Medium
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

from typing import List

class Solution0:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        ans = []
        def helper(s, k):
            # k is the index of digits
            if k == len(digits) - 1:
                for ch in phone[int(digits[k])]:
                    ans.append(s+ch)
                return
            for ch in phone[int(digits[k])]:
                helper(s+ch, k + 1)

        helper('', 0)
        return ans


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        ans = []
        s = ''

        def helper(s, k):
            # k is the index of digits
            if k == len(digits):
                ans.append(s)
                return
            for ch in phone[int(digits[k])]:
                helper(s+ch, k + 1)

        helper('', 0)
        return ans


x = '23'
print(Solution().letterCombinations(x))