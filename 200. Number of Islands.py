class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count=0
        while self.check1(grid)[0]:
            i,j=self.check1(grid)[1],self.check1(grid)[2]
            self.replaceGrid(grid,i,j)
            count+=1
        return count
    def check1(self,grid):
        i,j=-1,-1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    return True,i,j
        return False,i,j
    def replaceGrid(self,grid,i,j):
        grid[i][j]="*"
        if i-1 >= 0 and grid[i-1][j] == "1":
            self.replaceGrid(grid,i-1,j)
        if i+1 < len(grid) and grid[i+1][j] == "1":
            self.replaceGrid(grid,i+1,j)
        if j-1 >= 0 and grid[i][j-1] == "1":
            self.replaceGrid(grid,i,j-1)
        if j+1 < len(grid[0]) and grid[i][j+1] == "1":
            self.replaceGrid(grid,i,j+1)




s=Solution()
grid=[
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
print(s.numIslands(grid))