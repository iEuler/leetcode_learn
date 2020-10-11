"""
101. Symmetric Tree
Easy
https://leetcode.com/problems/symmetric-tree/
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Follow up: Solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def isSymmetric2(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            elif not left or not right:
                return False
            else:
                return left.val == right.val and isSymmetric2(left.left, right.right) and isSymmetric2(left.right,
                                                                                                       right.left)
        return not root or isSymmetric2(root.left, root.right)
