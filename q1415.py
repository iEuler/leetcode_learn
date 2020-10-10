"""
1415. The k-th Lexicographical String of All Happy Strings of Length n
Medium
https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/
A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.



Example 1:

Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
Example 2:

Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.
Example 3:

Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
Example 4:

Input: n = 2, k = 7
Output: ""
Example 5:

Input: n = 10, k = 100
Output: "abacbabacb"


Constraints:

1 <= n <= 10
1 <= k <= 100

"""


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * 1 << (n - 1):
            return ''
        other = [(1, 2), (0, 2), (0, 1)]
        ans = [(k-1) // (1 << (n - 1))]
        k2bit = bin((k-1) % (1 << (n - 1)))[2:]
        k2bit = '0'*(n-1-len(k2bit)) + k2bit
        # print(k2bit)
        for i in range(1, n):
            ans.append(other[ans[i-1]][int(k2bit[i-1])])
        letters = 'abc'

        return ''.join([letters[x] for x in ans])

n = 10
k = 100
print(Solution().getHappyString(n, k))