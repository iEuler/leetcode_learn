"""
241. Different Ways to Add Parentheses
https://leetcode.com/problems/different-ways-to-add-parentheses/

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
"""
from typing import List

class Solution1:
    def diffWaysToCompute(self, input: str) -> List[int]:
        calculated = []

        def helper(substr):
            if substr in calculated:
                return []
            calculated.append(substr)
            ans = []
            left1, left2 = 0, 0
            for k in range(len(substr)+1):
                if k == len(substr) and left1 == 0:
                    ans = [eval(substr)]
                    break
                if k == len(substr) or ( substr[k] in ['+', '-', '*'] and substr[k-1:k+1] != '(-'):
                    if left2 == left1:
                        left2 = k+1
                    else:
                        grouped_num = eval(substr[left1:k])
                        grouped_str = str(grouped_num) if grouped_num >= 0 else '('+str(grouped_num) + ')'
                        ans += helper(substr[:left1] + grouped_str + substr[k:])
                        left1, left2 = left2, k+1
            return ans

        return helper(input)


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:

        def helper(m,n,op):
            return m+n if op == '+' else m-n if op == '-' else m*n

        if input.isdigit():
            return [int(input)]
        ans = []
        for k in range(len(input)):
            if input[k] in '+-*':
                res1 = self.diffWaysToCompute(input[:k])
                res2 = self.diffWaysToCompute(input[k+1:])
                for m in res1:
                    for n in res2:
                        ans.append(helper(m,n,input[k]))
        return ans


x = "2-1-1"
x = "2*3-4*5"
print(Solution().diffWaysToCompute(x))