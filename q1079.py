"""
1079. Letter Tile Possibilities
Medium
https://leetcode.com/problems/letter-tile-possibilities/
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.



Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1


Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""
from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = ''.join(sorted(tiles))
        memo = {}
        def helper(s, k):
            if (s, k) not in memo:
                if k == 0:
                    memo[(s,k)] = 1
                else:
                    last, ans = '', 0
                    for i in range(len(s)):
                        if s[i] != last:
                            last = s[i]
                            ans += helper(s[:i]+s[i+1:], k-1)
                    memo[(s,k)] = ans
            return memo[(s,k)]

        ret = 0
        for k in range(1, len(tiles)+1):
            ret += helper(tiles, k)
        return ret

tiles = "CDC"
print(Solution().numTilePossibilities(tiles))