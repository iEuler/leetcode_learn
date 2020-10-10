"""
1307. Verbal Arithmetic Puzzle
Hard
https://leetcode.com/problems/verbal-arithmetic-puzzle/
Given an equation, represented by words on left side and the result on right side.

You need to check if the equation is solvable under the following rules:

Each character is decoded as one digit (0 - 9).
Every pair of different characters they must map to different digits.
Each words[i] and result are decoded as one number without leading zeros.
Sum of numbers on left side (words) will equal to the number on right side (result).
Return True if the equation is solvable otherwise return False.



Example 1:

Input: words = ["SEND","MORE"], result = "MONEY"
Output: true
Explanation: Map 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
Such that: "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652
Example 2:

Input: words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
Output: true
Explanation: Map 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->'3', 'Y'->4
Such that: "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214
Example 3:

Input: words = ["THIS","IS","TOO"], result = "FUNNY"
Output: true
Example 4:

Input: words = ["LEET","CODE"], result = "POINT"
Output: false


Constraints:

2 <= words.length <= 5
1 <= words[i].length, result.length <= 7
words[i], result contains only upper case English letters.
Number of different characters used on the expression is at most 10.

"""

from typing import List

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        if max([len(w) for w in words]) > len(result):
            return False
        lead_letters = set([w[0] for w in words + [result]])

        letters = []
        # two-element lists. First element is the letter, second element is the digit location, with a negative sign
        # for letters from "result". The letters are arranged from small digit to large digit.
        for k in range(1, len(result) + 1):
            for w in words:
                if len(w) >= k and w[-k] not in [x[0] for x in letters]:
                    letters.append((w[-k], k))
            letters.append((result[-k], -k))

        letter2num = {}
        num2letter = ['']*10
        nums = '0123456789'

        def helper(k):
            if k == len(letters):
                return True
            letter, digit = letters[k][0], letters[k][1]
            if digit < 0:
                # for letters in "result", check three cases.
                # 1. it's not defined and the target number (the sum of left lists) is not mapped. assign the map and
                # go to next letter
                # 2. it's already defined and not equal target number; or the target number has been mapped. Search
                # Fail.
                # 3. it's already defined and equals to target number. good. go to next letter

                left = sum([int(''.join([letter2num[ch] for ch in w[digit:]])) for w in words])
                if left < 10 ** (-digit-1):
                    return False
                num = int(str(left)[digit])  # target number
                if letter not in letter2num and not num2letter[num]:
                    letter2num[letter] = str(num)
                    num2letter[num] = letter
                    if helper(k + 1):
                        return True
                    letter2num.pop(letter)
                    num2letter[int(num)] = ''
                elif num2letter[num] != letter or (letter in letter2num and letter2num[letter] != str(num)):
                    return False
                else:
                    return helper(k + 1)

            else:
                # for letters not in "result", check two cases.
                # 1. it's not defined, search over all numbers which are not mapped.
                # 2. it's already defined. go to next letter
                if letter not in letter2num:
                    num_range = nums if letter not in lead_letters else nums[1:]
                    for num in num_range:
                        if not num2letter[int(num)]:
                            letter2num[letter] = num
                            num2letter[int(num)] = letter
                            if helper(k+1):
                                return True
                            letter2num.pop(letter)
                            num2letter[int(num)] = ''
                    return False
                else:
                    return helper(k + 1)

        return helper(0)

words = ["SEND","MORE"]
result = "MONEY"
print(Solution().isSolvable(words,result))