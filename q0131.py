"""
131. Palindrome Partitioning
Medium
https://leetcode.com/problems/palindrome-partitioning/
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

from typing import List

#
# class Solution1:
#     def partition(self, s: str) -> List[List[str]]:
#         ans = []
#         palindromes = []
#         ls = len(s)
#         for i in range(ls):
#             j = 0
#             while i - j - 1 >= 0 and i + j + 1 < ls and s[i - j - 1] == s[i + j + 1]:
#                 j += 1
#             if j:
#                 # palindromes += [(i - k - 1, i + k + 1) for k in range(j)]
#                 palindromes.append((i, i - j, i + j))
#             j = 0
#             while i - j >= 0 and i + j + 1 < ls and s[i - j] == s[i + j + 1]:
#                 j += 1
#             if j:
#                 # palindromes += [(i - k, i + k + 1) for k in range(j)]
#                 palindromes.append((i, i - j + 1, i + j))
#         palindromes.sort(key=lambda x: x[0])
#         lp = len(palindromes)
#
#         def helper(x):
#             # x is in the form of '011001', means the corresponding element in palindromes is used or not
#             right = -1
#             for ch in x:
#                 if ch == '1' and
#             pass
#
#         for k in range(2**lp , 2**(lp+1)):
#             k2bit = bin(k)[3:]
#             helper(k2bit)
#
#
#         print(palindromes)
#         return [[]]


class Solution0:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(s, path, answer):
            # base condition
            if not s:
                answer.append(path)
            for index in range(len(s)):
                # choose
                choose = s[:index + 1]
                if choose == choose[::-1]:
                    # Explore here
                    dfs(s[index + 1:], path + [choose], answer)

        answer = []
        dfs(s, [], answer)
        return answer


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        path = []

        def dfs(start):
            # base condition
            if start == len(s):
                answer.append(path[:])
            for index in range(start, len(s)):
                choose = s[start:index + 1]
                if choose == choose[::-1]:
                    path.append(choose)
                    dfs(index + 1)
                    path.pop()

        dfs(0)
        return answer
s = "hellelile"
print(Solution().partition(s))