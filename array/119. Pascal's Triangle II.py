class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res=[[1]]
        if rowIndex == 0:
            return res[-1]
        for i in range(1,rowIndex+1):
            temp=[1 for x in range(i+1)]
            for j in range(1,i):
                temp[j]=res[i-1][j-1]+res[i-1][j]
            res.append(temp)
        return res[-1]