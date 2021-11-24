class Solution:
    def rob(self, nums):
        
        return self.Robbery(nums,0,{})
    
    def Robbery(self,nums,currIndex,memo):
        
        if(currIndex>=len(nums)):
            return 0
        
        
        currKey=currIndex
        if currKey in memo:
            return memo[currKey]
        
        rob=nums[currIndex]+self.Robbery(nums,currIndex+2,memo)
        norob=self.Robbery(nums,currIndex+1,memo)
        
        memo[currKey]=max(rob,norob)
        return memo[currKey]


s=Solution()
nums=[1,2,3,1]
ans=s.rob(nums)
print(ans)
