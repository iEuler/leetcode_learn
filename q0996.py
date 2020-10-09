"""
996. Number of Squareful Arrays
Hard
https://leetcode.com/problems/number-of-squareful-arrays/
Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

Return the number of permutations of A that are squareful.  Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].



Example 1:

Input: [1,17,8]
Output: 2
Explanation:
[1,8,17] and [17,8,1] are the valid permutations.
Example 2:

Input: [2,2,2]
Output: 1


Note:

1 <= A.length <= 12
0 <= A[i] <= 1e9
"""

from typing import List
from math import sqrt
from collections import Counter
class Solution1:
    def numSquarefulPerms(self, A: List[int]) -> int:
        n = len(A)
        cnt = Counter(A)
        A = list(set(A))
        dic = {}
        for i in range(len(A)):
            dic[A[i]] = set()
            max_j = i + 1 if cnt[A[i]] > 1 else i
            for j in range(max_j):
                tmp = int(sqrt(A[i] + A[j]) + 0.1)
                if A[i] + A[j] == tmp*tmp:
                    dic[A[i]].add(A[j])
                    dic[A[j]].add(A[i])

        len_one = []
        for a in A:
            if not dic[a]:
                return 0
            if len(dic[a]) == 1 and cnt[list(dic[a])[0]] == 1:
                len_one += [a] * cnt[a]
        print(len_one)
        if len(len_one) > 2:
            return 0

        def dfs(num, k):
            if k == 0:
                return 1
            ans = 0
            for a in dic[num]:
                if cnt[a]:
                    cnt[a] -= 1
                    ans += dfs(a, k-1)
                    cnt[a] += 1
            return ans

        dic[-1] = set(len_one) if len(len_one) >= 1 else set(A)
        print(dic)
        ans = dfs(-1, n)
        return 2*ans if len(len_one) == 1 else ans


class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        n = len(A)
        cnt = Counter(A)
        A = list(set(A))
        dic = {}
        for i in range(len(A)):
            dic[A[i]] = []
            max_j = i + 1 if cnt[A[i]] > 1 else i
            for j in range(max_j):
                tmp = int(sqrt(A[i] + A[j]) + 0.1)
                if A[i] + A[j] == tmp * tmp:
                    dic[A[i]].append(A[j])
                    if A[i] != A[j]:
                        dic[A[j]].append(A[i])

        def dfs(num, k):
            if k == 0:
                return 1
            ans = 0
            for a in dic[num]:
                if cnt[a]:
                    cnt[a] -= 1
                    ans += dfs(a, k - 1)
                    cnt[a] += 1
            return ans

        dic[-1] = A
        return dfs(-1, n)


class Solution2:
    def numSquarefulPerms(self, A: List[int]) -> int:
        n = len(A)
        cnt = Counter(A)
        A = list(set(A))
        dic = {}
        num_cpty = {}
        for i in range(len(A)):
            dic[A[i]] = []
            num_cpty[A[i]] = 0
            max_j = i + 1 if cnt[A[i]] > 1 else i
            for j in range(max_j):
                tmp = int(sqrt(A[i] + A[j]) + 0.1)
                if A[i] + A[j] == tmp*tmp:
                    dic[A[i]].append(A[j])
                    if A[i] != A[j]:
                        dic[A[j]].append(A[i])
                        num_cpty[A[i]] += cnt[A[j]]
                        num_cpty[A[j]] += cnt[A[i]]
                    else:
                        num_cpty[A[i]] += cnt[A[i]] - 1

        len_one = []
        for a in A:
            if not dic[a]:
                return 0
            if num_cpty[a] == 1:
                len_one += [a] * cnt[a]
        if len(len_one) > 2:
            return 0

        def dfs(num, k):
            if k == 0:
                return 1
            ans = 0
            cpty = sorted([(a, num_cpty[a]) for a in dic[num] if cnt[a]], key=lambda x:x[1])
            for a,num_a in cpty:
                if num_a == 0:
                    return 0
                if cnt[a]:
                    cnt[a] -= 1
                    ans += dfs(a, k-1)
                    cnt[a] += 1
            return ans

        dic[-1] = list(set(len_one)) if len(len_one) >= 1 else A
        ans = dfs(-1, n)
        return 2 * ans if len(len_one) == 1 else ans


A = [1,17,8]
A = [1, 2, 3, 2, 6, 2,  6, 3]
A = [1, 6, 3, 3, 1, 8]
print(Solution().numSquarefulPerms(A))