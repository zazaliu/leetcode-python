# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.subTree(root.left, root.right)
        return True

    def subTree(self, l, r):
        if l == None and r == None:
            return True
        if l and r and l.val == r.val:
            return self.subTree(l.left, r.right) and self.subTree(l.right, r.left)
        return False