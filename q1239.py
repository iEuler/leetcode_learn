"""
1239. Maximum Length of a Concatenated String with Unique Characters
Medium
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.



Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26


Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
"""

from typing import List

class Solution:
    max_length = 0
    def maxLength(self, arr: List[str]) -> int:
        arr = [a for a in arr if len(set(a)) == len(a)]
        arr.sort(key=lambda s:len(s), reverse=True)

        def helper(seen, cur_length, k):
            extendable = False
            for i in range(k, len(arr)):
                a_set = set(arr[i])
                if not seen.intersection(a_set):
                    extendable = True
                    helper(seen.union(a_set), cur_length + len(arr[i]), i+1)
            if not extendable:
                self.max_length = max(self.max_length, cur_length)

        helper(set(), 0, 0)
        return self.max_length

arr = ["cha","r","act","ers"]
print(Solution().maxLength(arr))