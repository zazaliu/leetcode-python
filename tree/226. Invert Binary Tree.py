# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        if root.left or root.right:
            root.left,root.right=root.right,root.left
            if root.left:
                root.left=self.invertTree(root.left)
            if root.right:
                root.right=self.invertTree(root.right)
        return root