# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        基于Problem-102分层遍历，增加方向变量direction，依次选择是否反转每一层的节点顺序
        """
        res=[]
        if not root:
            return res
        myQueue=[]
        myQueue.append(root)
        direction = 1
        while myQueue:
            levelRes=[]
            for i in range(len(myQueue)):
                node=myQueue.pop(0)
                if node.left:
                    myQueue.append(node.left)
                if node.right:
                    myQueue.append(node.right)
                levelRes.append(node.val)
            res.append(levelRes) if direction else res.append(levelRes[::-1])
            direction=1-direction
        return res