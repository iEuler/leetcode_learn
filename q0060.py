"""
60. Permutation Sequence
Hard
https://leetcode.com/problems/permutation-sequence/

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        remain = [str(i+1) for i in range(9)]
        facto = [1]*n
        for i in range(2, n):
            facto[i] = i * facto[i-1]
        ans = [0]*n

        k -= 1
        for i in range(n-1):
            idx = k // facto[n - 1 - i]
            k = k % facto[n - 1 - i]
            ans[i] = remain.pop(idx)
        ans[-1] = remain[0]

        return ''.join(ans)

n = 4
k = 9
print(Solution().getPermutation(n,k))
