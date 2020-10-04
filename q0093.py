"""
93. Restore IP Addresses
Medium
https://leetcode.com/problems/restore-ip-addresses/
Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.



Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "1111"
Output: ["1.1.1.1"]
Example 4:

Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]
Example 5:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

"""

from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []

        ns = len(s)
        ans = []
        path = []
        def helper(start, need):
            # find (need) numbers in s[start:]
            if ns - start == need:
                ans.append(".".join(path + list(s[start:])))
            elif ns - start < need or ns - start > 3*need:
                return
            else:
                curlen = 1 if s[start] == '0' else 3
                for k in range(1,1+curlen):
                    if 0 <= int(s[start:start+k]) <= 255:
                        path.append(s[start:start+k])
                        helper(start+k, need-1)
                        path.pop()

        helper(0, 4)
        return ans

s = "25525511135"
s = "010010"
s = "101023"
s= "103574606193"
print(Solution().restoreIpAddresses(s))



