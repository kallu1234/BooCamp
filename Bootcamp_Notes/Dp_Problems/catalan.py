
class Solution:
    #Function to find the nth catalan number.
    def findCatalan(self,n):
        #return the nth Catalan number.
        return self.nthCatalan(n,{})
    def nthCatalan(self,n,memo):
        if n<=1:
            return 1
        
        key=n
        if key in memo:
            return memo[key]
        ways=0
        for i in range(0,n):
              ways+= self.nthCatalan(i,memo) * self.nthCatalan(n-i-1,memo)
        
        memo[key]=ways
        return memo[key]
