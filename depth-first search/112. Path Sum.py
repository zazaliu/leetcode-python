# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        res=[]
        if not root:
            return False
        nodeSum=root.val
        self.dfs(root,nodeSum,res)
        return sum in res
    def dfs(self,root,nodeSum,res):
        if not root.left and not root.right:
            res.append(nodeSum)
        if root.left:
            node=root.left
            self.dfs(root.left,nodeSum+node.val,res)
        if root.right:
            node=root.right
            self.dfs(root.right,nodeSum+node.val,res)