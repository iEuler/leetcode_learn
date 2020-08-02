"""
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

"""

class Soultion:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        mid, max_l, ans = 0, 1, s[0]
        while mid < n:
            left, right = mid-1, mid+1
            while right < n and s[right] == s[mid]:
                right += 1
            mid_l = right
            while right < n and left >= 0 and s[right] == s[left]:
                right += 1
                left -= 1
            if right-left-1 > max_l:
                max_l, ans = right-left-1, s[left+1:right]
            mid = mid_l

        return ans


s = "babad"
s = "abcbbbcbbbcda"
s = "bb"
print(Soultion().longestPalindrome(s))
