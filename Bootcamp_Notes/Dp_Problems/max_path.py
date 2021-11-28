
class Solution:
    def maximumPath(self, N, Matrix):
        # code here
        memo={}
        ans=0
        for i in range(0,N):
            tempans=self.MaxCost(N,0,i,Matrix,memo)
            ans=max(tempans,ans)
        return ans
    def MaxCost(self,N,row,col,Matrix,memo):
        
        if row>=N or col>=N or row<0 or col<0:
            return 0
        if(row==N-1):
            return Matrix[row][col]
        key=(row,col)
        #tc->O(n*m)
        if key in memo:
            return memo[key]
        down=Matrix[row][col]+self.MaxCost(N,row+1,col,Matrix,memo)
        dleft=Matrix[row][col]+self.MaxCost(N,row+1,col-1,Matrix,memo)
        dright=Matrix[row][col]+self.MaxCost(N,row+1,col+1,Matrix,memo)
       
        memo[key]= max(down,dleft,dright)
        return memo[key]
