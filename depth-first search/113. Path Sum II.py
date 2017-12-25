# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res=[]
        if not root:
            return []
        if root.left:
            self.dfs(root.left,[root.val],root.val,res,sum)
        if root.right:
            self.dfs(root.right,[root.val],root.val,res,sum)
        if not root.left and not root.right:
            return [[root.val]] if root.val == sum else []
        return res
    def dfs(self,root,nodeList,nodeSum,res,sum):
        if not root.left and not root.right:
            nodeSum+=root.val
            if nodeSum == sum:
                res.append(nodeList+[root.val])
        if root.left:
            self.dfs(root.left,nodeList+[root.val],nodeSum+root.val,res,sum)
        if root.right:
            self.dfs(root.right,nodeList+[root.val],nodeSum+root.val,res,sum)