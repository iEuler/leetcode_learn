"""
784. Letter Case Permutation
Medium
https://leetcode.com/problems/letter-case-permutation/

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.



Example 1:

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: S = "3z4"
Output: ["3z4","3Z4"]
Example 3:

Input: S = "12345"
Output: ["12345"]
Example 4:

Input: S = "0"
Output: ["0"]


Constraints:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""

from typing import List


class Solution0:
    # Runtime: 92 ms, faster than 20.46% of Python3 online submissions for Letter Case Permutation.
    # Memory Usage: 14.6 MB, less than 45.46% of Python3 online submissions for Letter Case Permutation.
    def letterCasePermutation(self, S: str) -> List[str]:
        ids = []
        for k, ch in enumerate(S):
            if 'a' <= ch <= 'z':
                ids.append((k, -1))
            elif 'A' <= ch <= 'z':
                ids.append((k, 1))
        n = len(ids)
        ans = []
        for i in range(1 << n, 1 << n + 1):
            i2bit = bin(i)[3:]
            s = S
            for k, ch in enumerate(i2bit):
                if ch == '1':
                    idx = ids[k][0]
                    s = s[:idx] + chr(ord(S[idx]) + ids[k][1] * 32) + s[idx+1:]
            ans.append(s)
        return ans


class Solution1:
    # Runtime: 88 ms, faster than 22.52% of Python3 online submissions for Letter Case Permutation.
    # Memory Usage: 14.5 MB, less than 48.43% of Python3 online submissions for Letter Case Permutation.
    def letterCasePermutation(self, S: str) -> List[str]:
        ids = []
        for k, ch in enumerate(S):
            if 'a' <= ch <= 'z':
                ids.append((k, -1))
            elif 'A' <= ch <= 'z':
                ids.append((k, 1))
        n = len(ids)
        ans = []

        for i in range(1 << n, 1 << n + 1):
            i2bit = bin(i)[3:]
            path = []
            last_idx = -1
            for k, ch in enumerate(i2bit):
                if ch == '1':
                    idx = ids[k][0]
                    path.append(S[last_idx+1:idx] + chr(ord(S[idx]) + ids[k][1] * 32))
                    last_idx = idx
            path.append(S[last_idx+1:])
            ans.append(''.join(path))
        return ans


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S:
            return ['']
        res = self.letterCasePermutation(S[1:])
        if S[0].isalpha():
            return [S[0].lower() + s for s in res] + [S[0].upper() + s for s in res]
        else:
            return [S[0] + s for s in res]

S = 'a1b2'
print(Solution().letterCasePermutation(S))