class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]: return False
        if matrix[0][0] > target or matrix[-1][-1] < target: return False
        row,column=len(matrix),len(matrix[0])
        if row > column:
            for i in range(column):
                s=[matrix[x][i] for x in range(row)]
                if self.binarySearch(s,target):return True
        else:
            for i in range(row):
                t=[matrix[i][x] for x in range(column)]
                if self.binarySearch(t,target):return True
        return False
    def binarySearch(self,s,target):
        left, right = 0, len(s) - 1
        while left < right:
            mid = left + (right - left) // 2
            if s[mid] > target:
                right = mid - 1
            else:
                left = mid
            if left + 1 == right:
                if s[left] == target or s[right] == target:
                    return True
                else:
                    return False
        if s[right] == target: return True
        else:return False



s=Solution()
matrix=[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target=30
print(s.searchMatrix(matrix,target))