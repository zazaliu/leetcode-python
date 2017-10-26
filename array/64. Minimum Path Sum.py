class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        动态规划（自底向上）  
        分析：  
        寻找从左上到右下的一条最短和路径，则，考虑从左上角位置出发，依次寻找出所有节点的最短和路径：  
        - 首先，构造一个路径和矩阵res,则res的第一行与第一列的最短路径和是确定的
        - 然后，依次从左到右从上到下考虑其他节点的最短路径和（选取该节点的左节点值与上节点值得最小值，加上本节点的值即为该节点的值）
        - 最后，res[-1][-1]即为所要求的值。
        """
        width, depth = len(grid[0]), len(grid)
        res = [[0 for x in range(width)] for x in range(depth)]
        res[0][0] = grid[0][0]
        for i in range(1, width):
            res[0][i] = res[0][i - 1] + grid[0][i]
        for i in range(1, depth):
            res[i][0] = res[i - 1][0] + grid[i][0]
        for i in range(1, depth):
            for j in range(1, width):
                res[i][j] = min(res[i - 1][j], res[i][j - 1]) + grid[i][j]
        return res[-1][-1]
