"""
98. Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def inRange(node, xmin, xmax):
            if not node: return True

            if node.val > xmin and node.val < xmax:
                return inRange(node.left, xmin, node.val) and inRange(node.right, node.val, xmax)
            else:
                return False

        return inRange(root, -1 * float('inf'), float('inf'))


class Solution2:
    def isValidBST(self, ary):
        """
        :type ary: array like a = [5, 1, 4, None, None, 3, 6]
        :rtype: bool
        """
        lvl, idx, totalnum = 1, 0, 2
        for k in range(len(ary)):
            if ary[k]:
                if k < totalnum-1:
                    leftidx = totalnum - 1 + idx * 2
                    rightidx = leftidx + 1
                    if leftidx >= len(ary):
                        return True
                    if ary[leftidx] and ary[leftidx] >= ary[k]:
                        return False
                    if ary[rightidx] and ary[rightidx] <= ary[k]:
                        return False
                    idx += 1
                else:
                    lvl += 1
                    idx = 0
                    totalnum *= 2
        return True


a = [5, 1, 4, None, None, 3, 6]
# a = [2,1,3]
a = [15, 10, 16, 5, 20, None, None]
print(Solution2().isValidBST(a))

