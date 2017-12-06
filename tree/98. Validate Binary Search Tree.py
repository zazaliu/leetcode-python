# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        二叉搜索树中序遍历结果为有序列表
        """
        res=[]
        if not root:res=[]
        self.InorderTraverse(root,res)
        # return sorted(res)
        return True if res == sorted(res) and len(list(set(res))) == len(res) else False
    def InorderTraverse(self, root, res):
        if not root:
            return
        self.InorderTraverse(root.left, res)
        res.append(root.val)
        self.InorderTraverse(root.right, res)