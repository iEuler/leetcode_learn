"""
907. Sum of Subarray Minimums
https://leetcode.com/problems/sum-of-subarray-minimums/

Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.



Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
"""

class Solution0():
    def sumSubarrayMins(self, A: list) -> int:
        modulo = 1000000007

        def min_sum(start, end):
            if start == end:
                return 0
            zmin = min(A[start:end])
            k = A[start:end].index(zmin)
            return ((k+1)*(end-start-k)*zmin + min_sum(start, start+k) + min_sum(start+k+1, end))%modulo

        return min_sum(0,len(A))


class Solution():
    def sumSubarrayMins(self, A: list) -> int:
        n = len(A)
        ids = [x[0] for x in sorted([(k, A[k]) for k in range(n)], key=lambda x: x[1])]

        modulo = 1000000007
        s = [-1, n]

        ans = 0
        for k in range(n):
            i = ids[k]
            start, end = max(0, len(s)-1-n+i), min(len(s)-1, i+1)
            while start <= end-2:
                j = (start+end)//2
                if s[j] > i:
                    end = j
                else:
                    start = j
            ans += ((i-s[start])*(s[end]-i)*A[i]) % modulo
            s = s[:end]+[i]+s[end:]

        return ans % modulo


class Solution2():
    def sumSubarrayMins(self, A: list) -> int:
        n = len(A)
        modulo = 1000000007

        q = []
        right = [1]*n
        for i in range(0,n):
            while q and A[q[-1]] >= A[i]:
                j = q.pop()
                right[j] = i - j
            q.append(i)
        while q:
            j = q.pop()
            right[j] = n - j

        q = []
        left = [1]*n
        for i in range(n-1,-1,-1):
            while q and A[q[-1]] > A[i]:
                j = q.pop()
                left[j] = j - i
            q.append(i)
        while q:
            j = q.pop()
            left[j] = j + 1

        ans = 0
        for i in range(n):
            ans = (ans + A[i]*left[i]*right[i]) % modulo

        print(left)
        print(right)
        return ans


class Solution3:
    def sumSubarrayMins(self, A: list) -> int:
        Stack = []
        res = 0
        A.append(-1)
        for i in range(len(A)):
            while Stack and A[Stack[-1]] >= A[i]:
                j = Stack.pop()
                k = -1 if len(Stack) == 0 else Stack[-1]
                res = (res + (j - k) * (i - j) * A[j]) % (10**9 + 7)
            Stack.append(i)
        return res

A = [3,1,2,4]
A = [71,55,82,55]
print(Solution3().sumSubarrayMins(A))
