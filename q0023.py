"""
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from queue import PriorityQueue

class Solution1:
    def mergeKLists(self, lists) -> ListNode:

        list_size = sum([bool(x) for x in lists])

        if not list_size:
            return None

        head_p = PriorityQueue()
        for k, x in enumerate(lists):
            if x:
                head_p.put((x.val, k))
                lists[k] = x.next

        head = ListNode()
        pre = head

        while not head_p.empty():
            y = head_p.get()
            if lists[y[1]]:
                head_p.put((lists[y[1]].val, y[1]))
            pre.next = ListNode(y[0])
            pre = pre.next

        return head.next


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        vals = []
        for listnode in lists:
            h = listnode
            while h:
                vals.append(h.val)
                h = h.next
        vals.sort()

        h1 = l1 = ListNode(0)
        for k in vals:
            l1.next = ListNode(k)
            l1 = l1.next

        return h1.next
