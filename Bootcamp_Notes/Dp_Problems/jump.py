class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.isPossible(nums,0,{})
    def isPossible(self,nums,currIndex,memo):
        
        if currIndex>=len(nums)-1:
                return True
        
        
        currKey=currIndex
        #Tc->O(n)*max(nums) like any max no in nums array 
        #sc->O(1) recursion-> O(n)->O(n)
        
        if currKey in memo:
            return memo[currKey]
        
        currJump=nums[currIndex]
        
        ans=False
        
        for i in range(1,currJump+1):
            tempans=self.isPossible(nums,currIndex+i,memo)
            ans= ans or tempans
        memo[currKey]=ans    
        return memo[currKey]
        

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
