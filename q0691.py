"""
691. Stickers to Spell Word
Hard
https://leetcode.com/problems/stickers-to-spell-word/
We are given N different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given target string by cutting individual letters from your collection of stickers and rearranging them.

You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

What is the minimum number of stickers that you need to spell out the target? If the task is impossible, return -1.

Example 1:

Input:

["with", "example", "science"], "thehat"
Output:

3
Explanation:

We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
Example 2:

Input:

["notice", "possible"], "basicbasic"
Output:

-1
Explanation:

We can't form the target "basicbasic" from cutting letters from the given stickers.
Note:

stickers has length in the range [1, 50].
stickers consists of lowercase English words (without apostrophes).
target has length in the range [1, 15], and consists of lowercase English letters.
In all test cases, all words were chosen randomly from the 1000 most common US English words, and the target was chosen as a concatenation of two random words.
The time limit may be more challenging than usual. It is expected that a 50 sticker test case can be solved within 35ms on average.

"""
from typing import List
from collections import Counter

class Solution0:
    # not working yet
    def minStickers(self, stickers: List[str], target: str) -> int:
        if target in stickers:
            return 1

        all_letters = set(''.join(stickers))
        cnt_target = {}
        for ch in target:
            if ch not in cnt_target:
                cnt_target[ch] = 1
                if ch not in all_letters:
                    return -1
            else:
                cnt_target[ch] += 1

        def helper(s):
            if s not in memo:
                ans = 0

                memo[s] = ans
            return memo[s]

        memo = {}
        ans = 0
        for k in range(1, len(target) - 1):
            match1, match2 = target[:k] in List, target[k:] in List
            if match1 and match2:
                return 2
            elif match1:
                ans = max(ans, 1 + helper(match2))
            elif match2:
                ans = max(ans, 1 + helper(match1))


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickers_counter = [Counter(st) for st in sorted(stickers, key=len, reverse=True)]
        dp = {'': 0}
        target = "".join(sorted(list(target)))

        def helper(target):
            if target not in dp:
                res = float('inf')
                for sticker in stickers_counter:
                    if target[0] in sticker:
                        nxt_tar = target
                        for s in sticker:
                            # delete target's characters which appear in sticker
                            nxt_tar = nxt_tar.replace(s, '', sticker[s])
                        if not nxt_tar:
                            res = 1
                            break
                        res = min(res, 1 + helper(nxt_tar))
                dp[target] = res
            return dp[target]

        res = helper(target)
        return res if res != float('inf') else -1

stickers = ["with", "example", "science"]
target = "thehat"
print(Solution().minStickers(stickers,target))