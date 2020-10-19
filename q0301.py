"""
301. Remove Invalid Parentheses
Hard
https://leetcode.com/problems/remove-invalid-parentheses/
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""

from typing import List
class Solution0:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        i = 0
        while i < len(s) and s[i] != '(':
            i += 1
        j = len(s) - 1
        while j > 0 and s[j] != ')':
            j -= 1
        j = max(j,i)
        head = ''.join(s[:i].split(')'))
        tail = ''.join(s[j + 1:].split('('))
        s = s[i:j+1]

        rev_dic = {'(': ')', ')': '('}
        rev = lambda a: rev_dic[a] if a in rev_dic else a

        def revString(s):
            return ''.join([rev(a) for a in s[::-1]])

        def get_splits(s):
            splits, extras = [], []
            # split s into substrings, such that each ')' in the substring is remove-able. rights are the number of
            # extra ')' in each substring. rights[k] < 0 means extra '(' needs to be removed, and the substring in
            # splits has been reverted, like '(a()(' => ')()a)'
            right, left, start = 0, 0, 0
            for k in range(len(s)):
                ch = s[k]
                if ch == '(':
                    left += 1
                    if left == 1 and right > 0:
                        splits.append(s[start:k])
                        extras.append(right)
                        right, start = 0, k
                elif ch == ')':
                    if left == 0:
                        right += 1
                    else:
                        left -= 1
            splits.append(s[start:])
            extras.append(right - left)
            return splits, extras

        splits_left, extras_left = get_splits(s)
        splits_right, extras_right = [], []
        if extras_left[-1] < 0:
            # revert and further split last substring
            s2 = revString(splits_left.pop())
            extras_left.pop()
            splits_right, extras_right = get_splits(s2)

        # s is divided into two sections, with extra ')' > 0 and <= 0

        def choose(n,k):
            # choose k numbers from [0,1,...,n-1], without repeat
            if k == 1:
                return [[i] for i in range(n)]
            ret = []
            for i in range(n - 1, k - 2, -1):
                for subpath in choose(i, k - 1):
                    ret.append(subpath+[i])
            return ret

        ans = set()
        def remove_extras(splits, extras, k_split, cleaned_string, pre_string):
            if k_split >= len(splits):
                ans.add(cleaned_string + pre_string)
                return
            s = pre_string + splits[k_split]
            m = extras[k_split]
            if m == 0:
                remove_extras(splits, extras, k_split+1, cleaned_string + s, '')
            else:
                idxs = [i for i in range(len(s)) if s[i] == ')']
                choices = choose(len(idxs), m)
                ret = set()
                for choice in choices:
                    s2 = ''
                    idx = [-1] + [idxs[k] for k in choice]
                    for i in range(m):
                        s2 += s[idx[i] + 1:idx[i + 1]]
                    if s2 not in ret:
                        ret.add(s2)
                        remove_extras(splits, extras, k_split + 1, cleaned_string + s2, s[idx[-1]+1:])

        remove_extras(splits_left, extras_left, 0, '', '')
        ans_L = list(ans)
        ans = set()
        remove_extras(splits_right, extras_right, 0, '', '')
        ans_R = list(ans)
        for k, x in enumerate(ans_R):
            ans_R[k] = revString(x)

        # print(s, splits_left, extras_left, splits_right, extras_right)
        # print(ans_L, ans_R)
        ans = []
        for sl in ans_L:
            for sr in ans_R:
                ans.append(head+sl+sr+tail)

        return ans

    def choose(self, n, k):
        # choose k numbers from [0,1,...,n-1], without repeat
        if k == 1:
            return [[i] for i in range(n)]
        ret = []
        for i in range(n - 1, k - 2, -1):
            for subpath in self.choose(i, k-1):
                ret.append(subpath[:]+[i])
        return ret


class Solution1:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        i = 0
        while i < len(s) and s[i] != '(':
            i += 1
        j = len(s) - 1
        while j > 0 and s[j] != ')':
            j -= 1
        j = max(j,i)
        head = ''.join(s[:i].split(')'))
        tail = ''.join(s[j + 1:].split('('))
        s = s[i:j+1]

        rev_dic = {'(': ')', ')': '('}
        rev = lambda a: rev_dic[a] if a in rev_dic else a

        def revString(s):
            return ''.join([rev(a) for a in s[::-1]])

        def get_splits(s):
            splits, extras = [], []
            # split s into substrings, such that each ')' in the substring is remove-able. rights are the number of
            # extra ')' in each substring. rights[k] < 0 means extra '(' needs to be removed, and the substring in
            # splits has been reverted, like '(a()(' => ')()a)'
            right, left, start = 0, 0, 0
            for k in range(len(s)):
                ch = s[k]
                if ch == '(':
                    left += 1
                    if left == 1 and right > 0:
                        splits.append(s[start:k])
                        extras.append(right)
                        right, start = 0, k
                elif ch == ')':
                    if left == 0:
                        right += 1
                    else:
                        left -= 1
            splits.append(s[start:])
            extras.append(right - left)
            return splits, extras

        splits_left, extras_left = get_splits(s)
        splits_right, extras_right = [], []
        if extras_left[-1] < 0:
            # revert and further split last substring
            s2 = revString(splits_left.pop())
            extras_left.pop()
            splits_right, extras_right = get_splits(s2)

        # s is divided into two sections, with extra ')' > 0 and <= 0

        splits_left.append('')
        splits_right.append('')
        extras_left.append(0)
        extras_right.append(0)

        def remove_extras(splits, extras, ans, k_split, cleaned_string, s, m):
            # to remove m ')' from s
            if k_split >= len(splits) - 1:
                ans.append(cleaned_string + s)
                return
            if m == 0:
                remove_extras(splits, extras, ans, k_split + 1, cleaned_string, s + splits[k_split + 1],
                              extras[k_split + 1])
            else:
                idxs = [i for i in range(len(s)) if s[i] == ')']
                for k in range(0, len(idxs) - m + 1):
                    if k == 0 or idxs[k] != idxs[k-1] + 1:
                        remove_extras(splits, extras, ans, k_split, cleaned_string + s[:idxs[k]], s[idxs[k] + 1:],
                                      m - 1)

        ans_L, ans_R = [], []
        remove_extras(splits_left, extras_left, ans_L, 0, '', splits_left[0], extras_left[0])
        remove_extras(splits_right, extras_right, ans_R, 0, '', splits_right[0], extras_right[0])
        for k, x in enumerate(ans_R):
            ans_R[k] = revString(x)

        ans = []
        for sl in ans_L:
            for sr in ans_R:
                ans.append(head+sl+sr+tail)

        return ans



class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        i = 0
        while i < len(s) and s[i] != '(':
            i += 1
        j = len(s) - 1
        while j > 0 and s[j] != ')':
            j -= 1
        j = max(j,i)
        head = ''.join(s[:i].split(')'))
        tail = ''.join(s[j + 1:].split('('))
        s = s[i:j+1]

        rev_dic = {'(': ')', ')': '('}
        rev = lambda a: rev_dic[a] if a in rev_dic else a

        def revString(s):
            return ''.join([rev(a) for a in s[::-1]])

        def get_splits(s):
            splits, extras = [], []
            # split s into substrings, such that each ')' in the substring is remove-able. rights are the number of
            # extra ')' in each substring. rights[k] < 0 means extra '(' needs to be removed, and the substring in
            # splits has been reverted, like '(a()(' => ')()a)'
            right, left, start = 0, 0, 0
            for k in range(len(s)):
                ch = s[k]
                if ch == '(':
                    left += 1
                    if left == 1 and right > 0:
                        splits.append(s[start:k])
                        extras.append(right)
                        right, start = 0, k
                elif ch == ')':
                    if left == 0:
                        right += 1
                    else:
                        left -= 1
            splits.append(s[start:])
            extras.append(right - left)
            return splits, extras

        splits_left, extras_left = get_splits(s)
        splits_right, extras_right = [], []
        if extras_left[-1] < 0:
            # revert and further split last substring
            s2 = revString(splits_left.pop())
            extras_left.pop()
            splits_right, extras_right = get_splits(s2)

        # s is divided into two sections, with extra ')' > 0 and <= 0

        splits_left.append('')
        splits_right.append('')
        extras_left.append(0)
        extras_right.append(0)
        ans = set()

        def remove_extras(splits, extras, k_split, cleaned_string, s, m):
            # to remove m ')' from s
            if k_split >= len(splits) - 1:
                ans.add(cleaned_string + s)
                return
            if m == 0:
                remove_extras(splits, extras, k_split + 1, cleaned_string, s + splits[k_split + 1], extras[k_split + 1])
            else:
                idxs = [i for i in range(len(s)) if s[i] == ')']
                for k in range(0, len(idxs) - m + 1):
                    if k == 0 or idxs[k] != idxs[k-1] + 1:
                        remove_extras(splits, extras, k_split, cleaned_string + s[:idxs[k]], s[idxs[k] + 1:], m - 1)

        remove_extras(splits_left, extras_left, 0, '', splits_left[0], extras_left[0])
        ans_L = list(ans)
        ans = set()
        remove_extras(splits_right, extras_right, 0, '', splits_right[0], extras_right[0])
        ans_R = list(ans)
        for k, x in enumerate(ans_R):
            ans_R[k] = revString(x)

        ans = []
        for sl in ans_L:
            for sr in ans_R:
                ans.append(head+sl+sr+tail)

        return ans

s = ')ac)(()x))(a())((()e)d(b'
s = ")o(v("
s = "(((k()(("
s = "(((()(()"
# s = "()())()"
print(Solution().removeInvalidParentheses(s))

# print(Solution().choose(5,3))

