"""
224. Basic Calculator
https://leetcode.com/problems/basic-calculator/

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""

class Solution:
    def calculate(self, s: str) -> int:
        ans = 0
        ops = [1]
        s += ' '
        y = ''
        cur_op = 1
        for x in s:
            if x not in ' +-()':
                y += x
            else:
                if y:
                    num = cur_op*int(y)
                    ans += num
                    y = ''

                if x in '+-':
                    cur_op = ops[-1] if x == '+' else -1*ops[-1]

                if x == '(':
                    ops.append(cur_op)
                elif x == ')':
                    ops.pop()
                    cur_op = ops[-1]

        return ans


s = " 2-1 + 2 "
s = "(1-((4+5+2)-3))+(6+8)"
print(Solution().calculate(s))