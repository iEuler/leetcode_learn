"""
227. Basic Calculator II
https://leetcode.com/problems/basic-calculator-ii/

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""

class Solution():
    def calculate(self, s: str) -> int:
        s += ' '
        lst = []
        y = ''
        op = ''
        for x in s:
            if x not in ' +-*/':
                y += x
            else:
                if y:
                    num = int(y)
                    if op == '-':
                        num = - num
                    elif op == '*':
                        num = lst.pop() * num
                    elif op == '/':
                        num_last = lst.pop()
                        num = num_last // num if num_last >= 0 else -(-num_last // num)
                    lst.append(num)
                if x != ' ':
                    op = x
                y = ''
        print(lst)
        return sum(lst)


s = "3+2*2"
s = " 3/2 "
s = " 3+5 / 2 "
print(Solution().calculate(s))