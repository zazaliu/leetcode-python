class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        """同Problem54"""
        res = [[0 for x in range(n)] for x in range(n)]
        start = 1
        left, right, top, bottom = 0, n - 1, 0, n - 1
        while left <= right and top <= bottom:
            for i in range(left, right+1):
                res[top][i] = start
                start += 1
            for i in range(top + 1, bottom + 1):
                res[i][right] = start
                start += 1
            for i in range(right - 1, left - 1, -1):
                res[bottom][i] = start
                start += 1
            for i in range(bottom - 1, top, -1):
                res[i][left] = start
                start += 1
            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
        return res
s=Solution()
print(s.generateMatrix(3))
