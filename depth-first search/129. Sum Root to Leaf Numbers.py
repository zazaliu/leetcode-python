# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[]
        if not root:
            return 0
        self.dfs(root,root.val,res)
        sum=0
        for i in res:
            sum+=i
        return sum
    def dfs(self,root,root2leaf,res):
        if not root.left and not root.right:
            res.append(root2leaf)
        if root.left:
            self.dfs(root.left,root2leaf*10+root.left.val,res)
        if root.right:
            self.dfs(root.right,root2leaf*10+root.right.val,res)