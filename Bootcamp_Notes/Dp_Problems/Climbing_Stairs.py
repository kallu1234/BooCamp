class Solution:
    def climbStairs(self, n):
           return self.findWays(0,n,{})
    def findWays(self,currStair,targetStair,memo):
        if currStair==targetStair:
            return 1
        if currStair>targetStair:
            return 0
        
        currKey=currStair
        if currKey in memo:
            return memo[currKey]
        
        
        
        oneJump=self.findWays(currStair+1,targetStair,memo)
        twoJump=self.findWays(currStair+2,targetStair,memo)
        
        memo[currKey]=oneJump+twoJump
        return memo[currKey]
        
        
        
        
s=Solution()
ans=s.climbStairs(4)
print(ans)
