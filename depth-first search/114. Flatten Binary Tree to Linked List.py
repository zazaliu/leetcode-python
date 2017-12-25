# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        """
        首先先序遍历二叉树，然后从根节点构造链表
        """
        res=[]
        cur=root
        self.preOrder(cur,res)
        if len(res) > 0:
            root.left=None
            for i in range(1,len(res)):
                root.left=None
                root.right=TreeNode(res[i])
                root=root.right
        print(res)
    def preOrder(self,root,res):
        if not root:
            return
        res.append(root.val)
        self.preOrder(root.left,res)
        self.preOrder(root.right,res)