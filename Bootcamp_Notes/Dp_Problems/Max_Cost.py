

class Solution:
    def maxCostClimbingStairs(self, cost):
        a=self.maxCost(cost,0,{})
        b=self.maxCost(cost,1,{})
        
        return max(a,b)
    
    def maxCost(self,cost,currIndex,memo):
        if currIndex==len(cost):
            return 0
        if currIndex>len(cost):
            return -1000
        
        currKey=currIndex
        if currKey in memo:
            return memo[currKey]
        
        onejump=cost[currIndex]+self.maxCost(cost,currIndex+1,memo)
        twojump=cost[currIndex]+self.maxCost(cost,currIndex+2,memo)
        
        memo[currKey]=max(onejump,twojump)
        return memo[currKey]
        
        
        
            
        
s=Solution()
cost=[10,15,20]
ans=s.maxCostClimbingStairs(cost)
print(ans)
