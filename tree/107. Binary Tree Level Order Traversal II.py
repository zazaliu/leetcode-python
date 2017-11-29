# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        二叉树分层遍历（Problem-102），输出结果反转
        """
        res=[]
        if not root:
            return res
        myQueue=[]
        myQueue.append(root)
        while myQueue:
            levelRes=[]
            for i in range(len(myQueue)):
                node=myQueue.pop(0)
                if node.left:
                    myQueue.append(node.left)
                if node.right:
                    myQueue.append(node.right)
                levelRes.append(node.val)
            res.append(levelRes)
        return res[::-1]