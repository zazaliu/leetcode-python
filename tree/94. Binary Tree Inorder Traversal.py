# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 递归实现
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        递归遍历实现
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


# 非递归实现
class Solution1:
    def inorderTraversal(self, root):
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
                myStack.append(node)
                node=node.left
            node=myStack.pop()
            res.append(node.val)
            node=node.right
        return res