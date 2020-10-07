"""
401. Binary Watch
Easy
https://leetcode.com/problems/binary-watch/
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

"""

from typing import List

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        hh = [['0'], ['1','2','4','8'], ['3','5','6','9','10'], ['7','11']]
        mm = [[] for k in range(6)]
        for k in range(64, 124):
            k2bit = len([1 for ch in bin(k)[3:] if ch == '1'])
            mm[k2bit].append('0'+str(k-64) if k < 74 else str(k-64))

        ans = []
        for nh in range(min(num, 3)+1):
            nm = num - nh
            if nm < 6:
                for h in hh[nh]:
                    for m in mm[nm]:
                        ans.append(h+':'+m)

        return ans

num = 1
print(Solution().readBinaryWatch(num))