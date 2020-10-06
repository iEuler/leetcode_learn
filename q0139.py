"""
139. Word Break
Medium
https://leetcode.com/problems/word-break/
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not set(s).issubset(set(''.join(wordDict))): return False
        max_word_length = max([len(word) for word in wordDict])
        memo = {}
        def dfs(s):
            if s not in memo:
                ans = False
                if s in wordDict:
                    ans = True
                else:
                    for index in range(min(len(s), max_word_length), 0, -1):
                        if s[:index] in wordDict and dfs(s[index:]):
                            ans = True
                            break
                memo[s] = ans
            return memo[s]

        return not s or dfs(s)

s = "leetcode"
wordDict = ["leet", "code"]
s = "applepenapple"
wordDict = ["apple", "pen"]
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
s = "ab"
wordDict = ["a","b"]

s = \
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]
print(Solution().wordBreak(s,wordDict))