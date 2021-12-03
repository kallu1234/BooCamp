
#code for minimum cost climbing stairs
class Solution:
    def minCostClimbingStairs(self, cost):
        #here we can start the currentStair from 0 or 1 and here we have to find the min cost for climbing 
        a=self.minCost(cost,0,{})
        b=self.minCost(cost,1,{})
        
        return min(a,b)
    
    def minCost(self,cost,currIndex,memo):
        #here if currIndex is equal to length of cost then return 0
        if currIndex==len(cost):
            return 0
        
        #here if currIndex is greater return 10000 or max_int value bcoz here we are finding minimum value 
        if currIndex>len(cost):
            return 1000
        
        #create a key of it 
        currKey=currIndex
        
        #check if currKey is present in memo or not 
        if currKey in memo:
            return memo[currKey]
        
        
        #calculate the cost of each stairs 
        onejump=cost[currIndex]+self.minCost(cost,currIndex+1,memo)
        twojump=cost[currIndex]+self.minCost(cost,currIndex+2,memo)
        
        #calculate the min cost of 1 jump and 2 jump 
        memo[currKey]=min(onejump,twojump)
        return memo[currKey]
        
        
        
            
        
s=Solution()
cost=[10,15,20]
ans=s.minCostClimbingStairs(cost)
print(ans)


# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
