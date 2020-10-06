"""
211. Design Add and Search Words Data Structure
Medium
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True


Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.
"""

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        self.loc = [0] # loc[l] record the start (inclusive) index of words of length l
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        l = len(word)
        for i in range(len(self.loc), l+2):
            self.loc.append(len(self.list))
        loc = self.loc[l+1]
        self.list[loc:loc] = [word]
        for i in range(l+1, len(self.loc)):
            self.loc[i] += 1        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        l = len(word)
        if l + 1 >= len(self.loc):
            return False
        start, end = self.loc[l], self.loc[l+1]
        for w in self.list[start:end]:            
                k, match = 0, True
                while k < len(word) and match:
                    if word[k] != w[k] and word[k] != '.':
                        match = False
                        break
                    k += 1
                if k == len(word):
                    return True
        return False

