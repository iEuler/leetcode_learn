"""
514. Freedom Trail
Hard
https://leetcode.com/problems/freedom-trail/

In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring", and use the dial to spell a specific keyword in order to open the door.

Given a string ring, which represents the code engraved on the outer ring and another string key, which represents the keyword needs to be spelled. You need to find the minimum number of steps in order to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at 12:00 direction. You need to spell all the characters in the string key one by one by rotating the ring clockwise or anticlockwise to make each character of the string key aligned at 12:00 direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:

You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step. The final purpose of the rotation is to align one of the string ring's characters at the 12:00 direction, where this character must equal to the character key[i].
If the character key[i] has been aligned at the 12:00 direction, you need to press the center button to spell, which also counts as 1 step. After the pressing, you could begin to spell the next character in the key (next stage), otherwise, you've finished all the spelling.
Example:



Input: ring = "godding", key = "gd"
Output: 4
Explanation:
For the first key character 'g', since it is already in place, we just need 1 step to spell this character.
For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
Also, we need 1 more step for spelling.
So the final output is 4.
Note:

Length of both ring and key will be in range 1 to 100.
There are only lowercase letters in both strings and might be some duplcate characters in both strings.
It's guaranteed that string key could always be spelled by rotating the string ring.

"""

from bisect import bisect_left
class Solution0:
    # This is not the minimum number
    def findRotateSteps(self, ring: str, key: str) -> int:
        n_ring, n_key = len(ring), len(key)
        dic = {}
        for k,ch in enumerate(ring):
            if ch not in dic:
                dic[ch] = [k]
            else:
                dic[ch].append(k)
        for ch in dic:
            first, last = dic[ch][0], dic[ch][-1]
            dic[ch] = [last-n_ring] + dic[ch] + [first+n_ring]
        ans = n_key
        loc = 0
        for ch in key:
            if ring[loc] != ch:
                idx = bisect_left(dic[ch], loc)
                if (loc - dic[ch][idx-1]) <= (dic[ch][idx] - loc):
                    new_loc = dic[ch][idx-1]
                    ans += loc - new_loc
                    loc = new_loc if new_loc >= 0 else new_loc+n_ring
                else:
                    new_loc = dic[ch][idx]
                    ans += new_loc - loc
                    loc = new_loc if new_loc < n_ring else new_loc - n_ring

        return ans


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        if not key or not ring:
            return 0
        key = ring[0] + key
        n_ring, n_key = len(ring), len(key)
        dic = {}
        for k,ch in enumerate(ring):
            if ch not in dic:
                dic[ch] = [k]
            else:
                dic[ch].append(k)
        target = {}
        for k in dic[key[-1]]:
            target[k] = 0
        for i in range(n_key - 2, -1, -1):
            if key[i] != key[i+1]:
                current = {}
                for cur in dic[key[i]]:
                    current[cur] = float('inf')
                    for nxt in target.keys():
                        step = min(nxt-cur, cur+n_ring-nxt) if nxt > cur else min(cur-nxt, nxt+n_ring-cur)
                        step += target[nxt]
                        current[cur] = min(current[cur], step)
                target = current

        return target[0] + n_key - 1

ring = "godding"
key = "gd"
print(Solution().findRotateSteps(ring,key))

