class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        area=0
        side=0
        memo={}
        n=len(matrix)
        m=len(matrix[0])
        for i in range(m-1):
            for j in range(n-1):
                if matrix[i][j]=='1':
                    side=self.Maxi(m,n,i,j,matrix,{})
        area=max(area,side*side)
        return area
    def Maxi(self,m,n,row,col,matrix,memo):
        if row>m or col>n or col<0 or row<0:
            return 0
       
        
        right=1+self.Maxi(m,n,row,col+1,matrix,memo)
        down=1+self.Maxi(m,n,row+1,col,matrix,memo)
        diag=1+self.Maxi(m,n,row+1,col+1,matrix,memo)
        
        return min(right,down,diag)
