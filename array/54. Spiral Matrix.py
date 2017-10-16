class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        if matrix == []:
            return res
        top,bottom,left,right = 0,len(matrix)-1,0,len(matrix[0])-1
        while left <= right and top <= bottom:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            for i in range(top+1,bottom+1):
                res.append(matrix[i][right])
            for i in range(right-1,left-1,-1):
                if top < bottom:
                    res.append(matrix[bottom][i])
            for i in range(bottom-1,top,-1):
                if left < right:
                    res.append(matrix[i][left])
            top,bottom,left,right = top+1,bottom-1,left+1,right-1
        return res