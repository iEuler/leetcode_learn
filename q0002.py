"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        lst = []
        nextdigit = 0
        while l1 or l2 or nextdigit:
            val = nextdigit
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            nextdigit = 0
            if val >= 10:
                val, nextdigit = val%10, 1
            lst.append(val)

        ans = ListNode(val=lst[-1])
        for k in range(len(lst)-2,-1,-1):
            val = lst[k]
            ans = ListNode(val=val, next=ans)

        return ans


def lst2Node(lst: list) -> ListNode:
    ans = ListNode(val=lst[-1])
    for k in range(len(lst) - 2, -1, -1):
        val = lst[k]
        ans = ListNode(val=val, next=ans)
    return ans


def node2lst(l: ListNode) -> list:
    ans = []
    while l:
        ans.append(l.val)
        l = l.next
    return ans


lst = [1,2,3]
lstNode = lst2Node(lst)
print(node2lst(lstNode))
