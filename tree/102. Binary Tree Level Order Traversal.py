# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        将每层结果划分为一个list
        """
        res = []
        if not root:
            return []
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            levelRes = []
            for i in range(len(myQueue)):
                node = myQueue.pop(0)
                if node.left:
                    myQueue.append(node.left)
                if node.right:
                    myQueue.append(node.right)
                levelRes.append(node.val)
            res.append(levelRes)
        return res

    def levelOrderWithoutList(self,root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        不考虑每层将每层结果重新分组，直接将所有结果按顺序输出
        """
        res=[]
        if not root:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            res.append(node.val)
            if node.left:
                myQueue.append(node.left)
            if node.right:
                myQueue.append(node.right)
