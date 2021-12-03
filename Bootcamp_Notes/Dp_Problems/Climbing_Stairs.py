class Solution:
    def climbStairs(self, n):
           return self.findWays(0,n,{})
    def findWays(self,currStair,targetStair,memo):
        #if currStair is equal to that finalstair then return 1
        if currStair==targetStair:
            return 1
        #if currStair is greater than target stair return 0
        if currStair>targetStair:
            return 0
        
        
        #make a key out of it 
        currKey=currStair
        
        #check if that key is present in memo or not
        if currKey in memo:
            return memo[currKey]
        
        #calculate the ways if we jump 1 stair or 2 stairs 
        
        oneJump=self.findWays(currStair+1,targetStair,memo)
        twoJump=self.findWays(currStair+2,targetStair,memo)
        
        memo[currKey]=oneJump+twoJump
        return memo[currKey]
        
        
        
        
s=Solution()
ans=s.climbStairs(4)
print(ans)


# Input:
# n = 4
# Output: 5
# Explanation:
# You can reach 4th stair in 5 ways. 
# Way 1: Climb 2 stairs at a time. 
# Way 2: Climb 1 stair at a time.
# Way 3: Climb 2 stairs, then 1 stair
# and then 1 stair.
# Way 4: Climb 1 stair, then 2 stairs
# then 1 stair.
# Way 5: Climb 1 stair, then 1 stair and
# then 2 stairs.
