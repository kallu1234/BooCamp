class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] or obstacleGrid[0][0]:
            return 0
        return self.TotalWays(obstacleGrid,m-1,n-1,0,0,{})
    def TotalWays(self,obstacleGrid,m,n,row,col,memo):
           
                                             
            if m==row and n==col :
                return 1
            if row>m or col>n or obstacleGrid[row][col]==1:
                return 0
           
            key=str(row)+"->"+str(col)
            if key in memo:
                return memo[key]
            down=self.TotalWays(obstacleGrid,m,n,row+1,col,memo)
            right=self.TotalWays(obstacleGrid,m,n,row,col+1,memo)
            memo[key]=down+right
            return memo[key]
