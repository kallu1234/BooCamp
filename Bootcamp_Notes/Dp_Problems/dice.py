class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        return self.TotalWays(d,f,target,{})%(10**9 + 7)
    
    def TotalWays(self,d,f,target,memo):
        
        if d==0 and target !=0 or  d!=0 and target==0 :
            return 0
        if d==0 and target==0:
            return 1
        
        
        key=(d,target)
        if key in memo:
            return memo[key]
        
        ans=0
        for current in range(1,f+1):
            tempAns=self.TotalWays(d-1,f,target-current,memo)
            ans+=tempAns
        memo[key]=ans
        return memo[key]
