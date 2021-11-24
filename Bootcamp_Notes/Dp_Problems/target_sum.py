class Solution:
    def findTargetSumWays(self, nums, target):
        return self.TotalWays(nums,target,0,{})
    def TotalWays(self,nums,target,currIndex,memo):
        if currIndex>=len(nums) and target!=0:
            return 0
        if currIndex>=len(nums) and target==0:
            return 1
        
        currKey=str(currIndex) + "->" +str(target)
        if currKey in memo:
            return memo[currKey]
        
        
        posSign=self.TotalWays(nums,target-nums[currIndex],currIndex+1,memo)
        negSign=self.TotalWays(nums,target+nums[currIndex],currIndex+1,memo)

        
        memo[currKey]=posSign+negSign
        return memo[currKey]

s=Solution()
nums=[1,1,1,1,1]
target=3
ans=s.findTargetSumWays(nums,target)
print(ans)
