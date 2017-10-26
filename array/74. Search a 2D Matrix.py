class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]:return False
        if target > matrix[-1][-1] or target < matrix[0][0]:
            return False
        column=[matrix[i][0] for i in range(len(matrix))]
        row=0
        for i in range(1,len(column)):
            if target < column[i]:
                break
            else:
                row=i
        # 二分查找
        low = 0
        height = len(matrix[0])-1
        while low <= height:
            mid = (low+height)//2
            if matrix[row][mid] < target:
                low = mid + 1

            elif matrix[row][mid] > target:
                height = mid - 1

            else:
                return True

        return False