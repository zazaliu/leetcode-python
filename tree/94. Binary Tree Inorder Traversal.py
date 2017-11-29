# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        self.InOrderTraverse(root, res)
        return res

    def InOrderTraverse(self, root, res):
        if not root:
            return
        self.InOrderTraverse(root.left, res)
        res.append(root.val)
        self.InOrderTraverse(root.right, res)
