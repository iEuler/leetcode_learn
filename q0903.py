"""
903. Valid Permutations for DI Sequence
Hard
https://leetcode.com/problems/valid-permutations-for-di-sequence/

We are given S, a length n string of characters from the set {'D', 'I'}. (These letters stand for "decreasing" and "increasing".)

A valid permutation is a permutation P[0], P[1], ..., P[n] of integers {0, 1, ..., n}, such that for all i:

If S[i] == 'D', then P[i] > P[i+1], and;
If S[i] == 'I', then P[i] < P[i+1].
How many valid permutations are there?  Since the answer may be large, return your answer modulo 10^9 + 7.


Example 1:

Input: "DID"
Output: 5
Explanation:
The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)


Note:

1 <= S.length <= 200
S consists only of characters from the set {'D', 'I'}.

"""



# https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
# If m is a prime, Euler's totient function phi(m) = m-1, i.e. a^(m-1) % m = 1. In other words a^(-1)%m = a^(m-2)%m

class Solution:
    def numPermsDISequence(self, S: str) -> int:
        memo = {}
        MOD = 10**9 + 7

        fac = [1] * (len(S)+1)
        for k in range(1, len(S)+1):
            fac[k] = (fac[k-1] * k) % MOD
        facinv = [pow(f, MOD-2, MOD) for f in fac]

        def binom(n, k):
            return fac[n] * facinv[n-k] % MOD * facinv[k] % MOD

        def reverse(s):
            return "".join([chr(141 - ord(ch)) for ch in s])

        def helper(s):
            # if s in memo or reverse(s) in memo:
            #     return memo[s] if s in memo else memo[reverse(s)]
            if s in memo:
                return memo[s]

            if len(s) <= 1:
                return 1

            ans = 0
            if s[0] == 'D':
                ans += helper(s[1:])
            if s[-1] == 'I':
                ans += helper(s[:-1])
            for k in range(len(s)-1):
                if s[k:k+2] == 'ID':
                    # ans += int(comb(len(s), k + 1) + 0.5) * (helper(s[:k]) * helper(s[k + 2:]))
                    ans += binom(len(s), k + 1) * (helper(s[:k]) * helper(s[k + 2:]))

            memo[s] = ans % MOD

            return memo[s]

        return helper(S)

import time
S = "IIDIIDDIDDDDIIDDIDIDIDDDDIDDDIIIIDDIDDDDIDIIDDIDID"
S = "IIDIIDDIDDDDIIDDIDIDIDDDDIDDDIIIIDDIDDDDIDIIDDIDID"
S = "IIDDIDDIIDDIDIDDIDDDDIIIDIDIDDDDDIIDIDDIDIIDIDDIIIDIIIIIIIIDIDIDIDDIDIIIIDDIIIIDDDDIIIDDIIDDIDIIIDDDDDDIIDIDDIIDDDDIIDDDIDIDDDIIIDIDIDIIIDDIDDDDDDDDIIDDIDDDIDDDIDDDDIIDIIIDDIDDDIDDIDDDIIDDIIIDIDIIDIDI"
# S = "IIDIIDDIDDDDIIDDIDIDIDDDDIIDDIDID"
# start_time = time.time()
print(Solution().numPermsDISequence(S))
print(Solution().numPermsDISequence(S[::-1]))
# print("Runtime = %s" % (time.time() - start_time))

# print(Solution().numPermsDISequence("IDDDI"))
# print(Solution().numPermsDISequence("IDDID"))
# print(Solution().numPermsDISequence("IDIDD"))
# print(Solution().numPermsDISequence("IIDDD"))
# print(Solution().numPermsDISequence("IDDDD"))