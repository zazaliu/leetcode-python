class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        res=[]
        for i in range(0,9):
            row=board[i]
            column=[board[x][i] for x in range(0,9)]
            row=[int(x) for x in row if x !='.']
            column = [int(x) for x in column if x != '.']
            res.append(row)
            res.append(column)
        square=[0,3,6]
        for i in square:
            for j in square:
                temp=board[i][j:j+3]+board[i+1][j:j+3]+board[i+2][j:j+3]
                temp=[int(x) for x in temp if x != '.']
                res.append(temp)
        return self.isvalid(res)

    def isvalid(self, res):
        for i in res:
            if len(i) != len(list(set(i))):
                return False
        return True

s=Solution()
board=[
    [".","8","7","6","5","4","3","2","1"],
    ["2",".",".",".",".",".",".",".","."],
    ["3",".",".",".",".",".",".",".","."],
    ["4",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".",".","."],
    ["6",".",".",".",".",".",".",".","."],
    ["7",".",".",".",".",".",".",".","."],
    ["8",".",".",".",".",".",".",".","."],
    ["9",".",".",".",".",".",".",".","."]
]
print(s.isValidSudoku(board))