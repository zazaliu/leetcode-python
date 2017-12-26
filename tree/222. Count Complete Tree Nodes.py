# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[]
        self.preOrder(root,res)
        return len(res)
    def preOrder(self,root,res):
        if not root:
            return
        res.append(root.val)
        self.preOrder(root.left,res)
        self.preOrder(root.right,res)