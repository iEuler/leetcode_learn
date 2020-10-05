"""
127. Word Ladder
Medium
https://leetcode.com/problems/word-ladder/
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

from typing import List

class Solution:
    #  exceed time limit
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nList = len(wordList)

        remains = [1]*nList
        for k in range(nList):
            if wordList[k] == endWord:
                remains[k] = 0
                prevList = [k]
                break

        def isNeighbor(word1, word2):
            return len([1 for k in range(len(word1)) if word1[k] != word2[k]]) == 1

        dist = 0
        while True:
            dist += 1
            nextList = []
            for idx_prev in prevList:
                word = wordList[idx_prev]
                if isNeighbor(beginWord, word):
                    return dist + 1
                for k in range(nList):
                    if remains[k]:
                        word2 = wordList[k]
                        if isNeighbor(word, word2):
                            nextList.append(k)
                            remains[k] = 0
            if not nextList:
                return 0
            prevList = nextList[:]

class Solution0:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord == endWord:
            return 1
        nWord, nList = len(endWord), len(wordList)

        wordList = set(wordList)
        wordList.discard(endWord)
        front, back = set([beginWord]), set([endWord])

        letters = 'abcdefghijklmnopqrstuvwxyz'

        dist = 0
        while True:
            dist += 1
            if len(front) > len(back):
                front, back = back, front
            newFront = set()
            for word1 in front:
                for k in range(nWord):
                    for s in letters:
                        word = word1[:k] + s + word1[k + 1:]
                        if word in back:
                            return dist + 1
                        if word in wordList:
                            newFront.add(word)
            if not newFront:
                return 0
            wordList -= newFront
            front = newFront



class Solution1:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        wordList = set(wordList)

        if endWord not in wordList: return 0
        if beginWord == endWord: return 1

        ans = 2
        front = set([beginWord])
        back = set([endWord])
        wordList.discard(endWord)

        l = len(endWord)
        letters = 'abcdefghijklmnopqrstuvwxyz'

        while front and back:
            if len(front) > len(back):
                front, back = back, front
            # print(targetLists)

            newFront = set()
            for word1 in front:
                for k in range(l):
                    for s in letters:
                        word = word1[:k] + s + word1[k + 1:]
                        if word in back:
                            return ans
                        if word in wordList:
                            newFront.add(word)

            wordList -= newFront
            front = newFront
            ans += 1

        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
# wordList = ["hot","dot","dog","lot","log"]
print(Solution().ladderLength(beginWord,endWord,wordList))