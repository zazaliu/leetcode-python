# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        if not root:
            return res
        self.PostOrder(root, res)
        return res
    def PostOrder(self, root, res):
        if not root:
            return
        self.PostOrder(root.left, res)
        self.PostOrder(root.right, res)
        res.append(root.val)