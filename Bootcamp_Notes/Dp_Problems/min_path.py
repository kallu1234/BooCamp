class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.findPath(grid,len(grid)-1,len(grid[0])-1,0,0,{})
    
    def findPath(self,grid,row,col,i,j,memo):
        if i>row or j>col:
            return 9999
        if i==row and j==col:
            return grid[i][j]
        key=str(i) + "->" + str(j)
        if key in memo:
            return memo[key]
        
        rightMove=grid[i][j]+self.findPath(grid,row,col,i+1,j,memo)
        leftMove=grid[i][j]+self.findPath(grid,row,col,i,j+1,memo)
        
        memo[key]=min(rightMove,leftMove)
        return memo[key]
