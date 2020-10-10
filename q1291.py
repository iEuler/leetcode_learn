"""
1291. Sequential Digits
Medium
https://leetcode.com/problems/sequential-digits/

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.



Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]


Constraints:

10 <= low <= high <= 10^9
"""

from typing import List

class Solution1:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nl, nh = len(str(low)), len(str(high))
        ans = []
        sequential = '123456789'
        for n in range(nl, min(nh+1,10)):
            start, delta = int(sequential[:n]), int('1'*n)
            k_min = 0 if n > nl else max(-(-(low-start) // delta), 0)
            k_max = 9 - n if n < nh else (min(high, int(sequential[-n:]))-start) // delta
            print(n, k_min, k_max)
            ans += [start + k*delta for k in range(k_min, k_max + 1)]

        return ans


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nl, nh = len(str(low)), len(str(high))
        ans = []
        sequential = '123456789'
        for n in range(nl, min(nh+1,10)):
            for k in range(10-n):
                if low <= int(sequential[k:k+n]) <= high:
                    ans.append(int(sequential[k:k+n]))
        return ans

low = 100
high = 300
# low = 178546104
# high = 812704742
print(Solution().sequentialDigits(low, high))