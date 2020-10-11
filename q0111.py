"""
111. Minimum Depth of Binary Tree
Easy
https://leetcode.com/problems/minimum-depth-of-binary-tree/
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution0:
    # depth first search
    ans = float('inf')

    def minDepth(self, root: TreeNode) -> int:

        def helper(node, level):
            if not node.left and not node.right:
                self.ans = min(self.ans, level + 1)
            elif level > self.ans:
                return
            else:
                if node.left:
                    helper(node.left, level + 1)
                if node.right:
                    helper(node.right, level + 1)

        if root:
            helper(root, 0)
        else:
            self.ans = 0
        return self.ans


from queue import Queue

class Solution:
    # depth first search

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = Queue()
        q.put((root, 0))
        while not q.empty():
            node, lvl = q.get()
            if not node.left and not node.right:
                return lvl + 1
            if node.left:
                q.put((node.left, lvl+1))
            if node.right:
                q.put((node.right, lvl+1))


