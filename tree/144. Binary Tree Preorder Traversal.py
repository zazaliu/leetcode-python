# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 递归方式实现
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        递归遍历
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


# 非递归方式实现

class Solution1:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        if not root:
            return res
        myStack=[]
        node=root
        while node or myStack:
            while node:
                res.append(node.val)
                myStack.append(node)
                node=node.left
            node=myStack.pop()
            node=node.right
        return res