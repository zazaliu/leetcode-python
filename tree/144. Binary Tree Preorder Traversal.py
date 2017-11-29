# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        if not root:
            return res
        self.PreOrder(root,res)
        return res
    def PreOrder(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.PreOrder(root.left, res)
        self.PreOrder(root.right, res)