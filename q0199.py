"""
199. Binary Tree Right Side View
Medium
https://leetcode.com/problems/binary-tree-right-side-view/
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from queue import Queue
from typing import List

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        ans = []
        q = Queue()
        q.put((root, 0))
        while not q.empty():
            node, lvl = q.get()
            if node:
                if lvl + 1 > len(ans):
                    ans.append(node.val)
                q.put((node.right, lvl + 1))
                q.put((node.left, lvl + 1))

        return ans