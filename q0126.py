"""
126. Word Ladder II
Hard
https://leetcode.com/problems/word-ladder-ii/
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

from typing import List
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        if beginWord == endWord:
            return [[beginWord]]
        nWord, nList = len(endWord), len(wordList)
        # if nWord == 1:
        #     return [[beginWord, endWord]]

        neighbors = {beginWord: []}
        for w in wordList:
            neighbors[w] = []

        wordSet = set(wordList)
        wordSet.discard(endWord)
        wordSet.discard(beginWord)
        front, back = set([beginWord]), set([endWord])

        letters = 'abcdefghijklmnopqrstuvwxyz'
        reversed = 0
        connected = False
        while not connected:
            if len(front) > len(back):
                front, back = back, front
                reversed = 1 - reversed
            newFront = set()
            for word1 in front:
                for k in range(nWord):
                    for s in letters:
                        word = word1[:k] + s + word1[k + 1:]
                        if word in back:
                            connected = True
                        if word in back or word in wordSet:
                            newFront.add(word)
                            if reversed:
                                neighbors[word].append(word1)
                            else:
                                neighbors[word1].append(word)
            if not newFront:
                return []
            wordSet -= newFront
            front = newFront

        ans = []
        path = [beginWord]

        def backtracking(word):
            if word == endWord:
                ans.append(path[:])
                return
            for w in neighbors[word]:
                path.append(w)
                backtracking(w)
                path.pop()
        backtracking(beginWord)
        return ans


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
# wordList = ["hot","dot","dog","lot","log"]

print(Solution().findLadders(beginWord,endWord,wordList))