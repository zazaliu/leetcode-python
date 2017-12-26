class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        """
        DP算法：从右下角依次求出从当前位置到右下角位置所需最小生命值即可
        """
        res = [[0 for x in range(len(dungeon[0]))] for y in range(len(dungeon))]
        res[-1][-1] = 1
        for i in range(len(dungeon) - 2, -1, -1):
            res[i][-1] = max(1, res[i + 1][-1] - dungeon[i + 1][-1])
        for i in range(len(dungeon[0]) - 2, -1, -1):
            res[-1][i] = max(1, res[-1][i + 1] - dungeon[-1][i + 1])
        for i in range(len(dungeon) - 2, -1, -1):
            for j in range(len(dungeon[0]) - 2, -1, -1):
                right = max(1, res[i][j + 1] - dungeon[i][j + 1])
                bottom = max(1, res[i + 1][j] - dungeon[i + 1][j])
                res[i][j] = min(right, bottom)
        return max(1, res[0][0] - dungeon[0][0])


s=Solution()
dungeon=[[0]]
print(s.calculateMinimumHP(dungeon))