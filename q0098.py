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
    def isValidBST(self,ary):
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
print(Solution2().isValidBST(a))

