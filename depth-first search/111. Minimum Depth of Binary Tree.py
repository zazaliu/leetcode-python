# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = []
        if not root.left and not root.right:
            return 1
        if root.left:
            self.dfs(root.left, 1, res)
        if root.right:
            self.dfs(root.right, 1, res)
        res.sort()
        return res[0]

    def dfs(self, root, depth, res):
        if not root.left and not root.right:
            res.append(depth + 1)
        if root.left:
            self.dfs(root.left, depth + 1, res)
        if root.right:
            self.dfs(root.right, depth + 1, res)
