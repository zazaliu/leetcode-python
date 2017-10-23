class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        width,depth=len(obstacleGrid[0]),len(obstacleGrid)
        if obstacleGrid[0][0] or obstacleGrid[-1][-1] == 1:return 0
        res=obstacleGrid
        for i in range(depth):
            for j in range(width):
                res[i][j]=1-res[i][j]
        for i in range(1,width):
            if res[0][i] != 0:res[0][i]=res[0][i-1]
        for i in range(1,depth):
            if res[i][0] != 0:res[i][0]=res[i-1][0]
        for i in range(1,depth):
            for j in range(1,width):
                if res[i][j] != 0:res[i][j]=res[i-1][j]+res[i][j-1]
        return res
s=Solution()
test=[[0,0],[1,1],[0,0]]
print(s.uniquePathsWithObstacles(test))