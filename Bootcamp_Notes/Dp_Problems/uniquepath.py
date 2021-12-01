class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.findWays(m-1,n-1,0,0,{})
    def findWays(self,m,n,row,col,memo):
          
            if m==row and n==col:
                return 1
            if row>m or col>n:
                return 0
             
            key=str(row)+"->"+str(col)
            if key in memo:
                return memo[key]
            down=self.findWays(m,n,row+1,col,memo)
            right=self.findWays(m,n,row,col+1,memo)
            memo[key]=down+right
            return memo[key]
            
       
