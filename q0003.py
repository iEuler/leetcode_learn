"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left, max_length = 0, 1
        dct = {s[0]:0}
        s += s[-1]
        for right in range(1,len(s)):
            if s[right] not in dct or dct[s[right]] < left:
                dct[s[right]] = right
            else:
                max_length = max(max_length, right-left)
                left = dct[s[right]]+1
                dct[s[right]] = right

        return max_length


s = "pwwkew"
# s = "abcabcbb"
# s = "bbbbb"
# s = "au"
# s = "dvdf"
print(Solution().lengthOfLongestSubstring(s))
