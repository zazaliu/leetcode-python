class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res=[[1]]
        if numRows == 1:
            return res
        for i in range(1,numRows):
            temp=[1 for x in range(i+1)]
            for j in range(1,i):
                temp[j]=res[i-1][j-1]+res[i-1][j]
            res.append(temp)
        return res