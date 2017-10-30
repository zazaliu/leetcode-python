class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        """
        从三角形第二行开始计算每个位置的最短路径，每个位置的最短路径都等当前位置的值加上上一行对应可以到达该位置
        的两个节点的最短路径的最小值，最后直至整个三角形内容均填充为从三角形顶点到达任意位置的路径最小值，然后输出
        该三角形最后一行最小值即为结果。
        """
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i - 1][0]
            triangle[i][-1] += triangle[i - 1][-1]
            for j in range(1, i):
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[-1])
