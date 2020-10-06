"""
140. Word Break II
Hard
https://leetcode.com/problems/word-break-ii/
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not set(s).issubset(set(''.join(wordDict))): return []
        max_word_length = max([len(word) for word in wordDict])
        memo = {}
        memo[''] = ['']

        def dfs(s):
            if not s:
                return True
            if s not in memo:
                ans = []
                for index in range(min(len(s), max_word_length), 0, -1):
                    if s[:index] in wordDict and dfs(s[index:]):
                        for sub in memo[s[index:]]:
                            ans.append(s[:index] + ' ' + sub)
                memo[s] = ans
            return bool(memo[s])

        dfs(s)
        return [x[:-1] for x in memo[s]]


s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
print(Solution().wordBreak(s, wordDict))