class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        """
        方法一：O(m+n)
        """
        row,column=[],[]
        width,depth=len(matrix[0]),len(matrix)
        for i in range(depth):
            for j in range(width):
                if matrix[i][j] == 0:
                    row.append(i)
                    column.append(j)
        row,column=list(set(row)),list(set(column))
        for i in range(len(row)):
            for j in range(width):
                matrix[row[i]][j]=0
        for i in range(len(column)):
            for j in range(depth):
                matrix[j][column[i]]=0
        """
        方法二：O(1)
        """
        width,depth=len(matrix[0]),len(matrix)
        for i in range(depth):
            for j in range(width):
                if matrix[i][j] == 0:
                    for k in range(width):
                        if matrix[i][k] != 0:
                            matrix[i][k]="m"
                    for k in range(depth):
                        if matrix[k][j] != 0:
                            matrix[k][j]="m"
        for i in range(depth):
            for j in range(width):
                if matrix[i][j] == "m":
                    matrix[i][j]=0