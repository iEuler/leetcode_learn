"""
282. Expression Add Operators
https://leetcode.com/problems/expression-add-operators/

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"]
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
"""

from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        def helper(s, k):
            if k == 0:
                if s[0] == '0' and len(s) > 1 and s[1] not in '+-*':
                    return []
                return [s] if eval(s) == target else []
            ans = helper(s, k - 1)
            if s[k] != '0' or k == len(s)-1 or s[k+1] in '+-*':
                ans += helper(s[:k] + '+' + s[k:], k - 1)\
                       + helper(s[:k] + '-' + s[k:], k - 1)\
                       + helper(s[:k] + '*' + s[k:], k - 1)
            return ans

        if not num:
            return []
        return helper(num, len(num)-1)


num = "105"
target = 5
num = "123"
target = 6
num = "00"
target = 0
num = ""
target = 5
print(Solution().addOperators(num,target))