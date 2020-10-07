"""
526. Beautiful Arrangement
Medium
https://leetcode.com/problems/beautiful-arrangement/
Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.


Now given N, how many beautiful arrangements can you construct?

Example 1:

Input: 2
Output: 2
Explanation:

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.


Note:

N is a positive integer and will not exceed 15.

"""


class Solution0:
    # NOT WORKING :(
    def countArrangement(self, N: int) -> int:
        if N <= 3:
            return N

        prime = [2, 3]

        def nFactor(n):
            # number of factors of n, excluding 1 and itself
            factors = {}
            while n > 1:
                for p in prime:
                    if n % p == 0:
                        if p not in factors:
                            factors[p] = 1
                        else:
                            factors[p] += 1
                        n = n // p
                        break
                if not factors:
                    prime.append(n)
                    return 0
            ans = 1
            for p in factors.keys():
                ans *= factors[p] + 1
            return ans - 2


        ret = 3
        for n in range(4, N+1):
            # Suppose there are a_{n-1} beautiful arrays for n-1.
            # claim a_n = a_{n-1} * n / (n-1) * (1 + nFactor(n)), and for each i in [1,n], the number of beautiful
            # arrays with 1 at i-th position is b_n = a_n / n. Can be approved by mathematical induction.
            # From n - 1 to n, three cases:
            # 1. put n directly at n-th position -- a_{n-1}
            # 2. switch n and 1, if 1 is at i-th position with i a factor of n.
            #   note that for each such i, there are a_{n-1}/(n-1) arrays.
            #   so, it's a total of (1 + nFactor(n)) * a_{n-1}/(n-1)
            # 3. switch n and k, where k > 1 is a factor of n. -- nFactor(n) * a_{n-1}
            ret = (ret//(n-1) + ret) * (nFactor(n) + 1)

        return ret


class Solution1:
    def countArrangement(self, N: int) -> int:

        ret = []
        path = []

        def fn(i):
            """Return the number of beautiful arrangements of N numbers."""
            if i == 0:
                ret.append(path[::-1])
                return 1  # boundary condition
            ans = 0
            for k in range(1, N + 1):
                if k not in seen and (k % i == 0 or i % k == 0):
                    seen.add(k)
                    path.append(k)
                    ans += fn(i - 1)
                    seen.remove(k)
                    path.pop()
            return ans

        seen = set()
        a = fn(N)
        for r in ret:
            print(r)
        return a

class Solution2:
    def countArrangement(self, N: int) -> int:

        factors = [[] for _ in range(N+1)]
        factors[1].append(1)
        for k in range(2, N+1):
            factors[k] = [1, k]
            for i in range(2,k):
                if k%i == 0:
                    factors[k].append(i)

        path = []
        def helper(i):
            # try to fill the i-th position
            if i == 0:
                return 1
            ans = 0
            multiples = [i * j for j in range(2, N//i + 1)]
            for k in factors[i] + multiples:
                if k not in path:
                    path.append(k)
                    ans += helper(i-1)
                    path.pop()
            return ans

        return helper(N)

class Solution:
    def countArrangement(self, N: int) -> int:
        memo = {}
        def helper(i, s):
            # try to fill the i-th position
            if i == 0:
                return 1
            if s not in memo:
                ans = 0
                for k, n in enumerate(s):
                    if n%i == 0 or i%n == 0:
                        ans += helper(i-1, s[:k]+s[k+1:])
                memo[s] = ans
            return memo[s]

        return helper(N, tuple(range(1,N+1)))

N = 7
print(Solution().countArrangement(N))

