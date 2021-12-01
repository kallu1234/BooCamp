class Solution:
    def numTrees(self, n: int) -> int:
       
        #return the nth Catalan number.
        return self.nthBST(n,{})
    def nthBST(self,n,memo):
        if n<=1:
            return 1
        
        key=n
        #Tc->2^n
        #sc->O(n)
        if key in memo:
            return memo[key]
        ways=0
        for i in range(0,n):
            ways+= self.nthBST(i,memo) * self.nthBST(n-i-1,memo)
        
        memo[key]=ways
        return memo[key]

        
