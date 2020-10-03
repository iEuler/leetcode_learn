"""
216. Combination Sum III
Medium
https://leetcode.com/problems/combination-sum-iii/

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.



Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations. [1,2,1] is not valid because 1 is used twice.
Example 4:

Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.
Example 5:

Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
​​​​​​​There are no other valid combinations.


Constraints:

2 <= k <= 9
1 <= n <= 60

"""

from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def dp(start, k, n):
            if start > 10 - k or n < k * (k - 1 + 2 * start) / 2 or n > (19 - k) * k / 2:
                return []
            if k == 1:
                return [[n]]
            else:
                ans = []
                for lst in dp(start + 1, k - 1, n - start):
                    ans.append([start] + lst)
                return ans + dp(start+1, k, n)

        return dp(1, k, n)


k = 3
n = 9
print(Solution().combinationSum3(k, n))