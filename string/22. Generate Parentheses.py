class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        self.generateParent(n,n,"",res)
        return res
    def generateParent(self, left, right, parentStr, res):
        if left == 0 and right == 0:
            res.append(parentStr)
        if left > 0:
            self.generateParent(left-1,right,parentStr+'(',res)
        if right > left:
            self.generateParent(left,right-1,parentStr+')',res)