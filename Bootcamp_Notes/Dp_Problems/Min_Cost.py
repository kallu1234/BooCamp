
#code for minimum cost climbing stairs
class Solution:
    def minCostClimbingStairs(self, cost):
        a=self.minCost(cost,0,{})
        b=self.minCost(cost,1,{})
        
        return min(a,b)
    
    def minCost(self,cost,currIndex,memo):
        if currIndex==len(cost):
            return 0
        if currIndex>len(cost):
            return 1000
        
        currKey=currIndex
        if currKey in memo:
            return memo[currKey]
        
        onejump=cost[currIndex]+self.minCost(cost,currIndex+1,memo)
        twojump=cost[currIndex]+self.minCost(cost,currIndex+2,memo)
        
        memo[currKey]=min(onejump,twojump)
        return memo[currKey]
        
        
        
            
        
s=Solution()
cost=[10,15,20]
ans=s.minCostClimbingStairs(cost)
print(ans)
