# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 递归实现
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        递归遍历实现
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


# 非递归实现1
class Solution1:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        if not root:
            return res
        myStack=[]
        node=root
        myStack.append(node)
        while myStack:
            node=myStack.pop()
            if node.left:
                myStack.append(node.left)
            if node.right:
                myStack.append(node.right)
            res.append(node.val)
        return res[::-1]

# 非递归实现2——后序遍历等价于将遍历左右顺序调换的先序遍历结果的反转，
# 即先采用先序遍历（左右子树访问顺序反转），然后将遍历结果反转即可
class Solution2:
    def postorderTraversal(self, root):
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
                res.append(node.val)
                node=node.right
            node=myStack.pop()
            node=node.left
        return res[::-1]