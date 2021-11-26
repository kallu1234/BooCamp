class Solution:
    def jump(self, nums):
        return self.minJumps(nums,0,{})
    def minJumps(self,nums,currIndex,memo):
        if currIndex>=len(nums)-1:
            return 0
        
        answer=10000
        key=currIndex
        if key in memo:
            return memo[key]
        
        currJump=nums[currIndex]
        for i in range(1,currJump+1):
            ans=1+self.minJumps(nums,currIndex+i,memo)
            answer=min(ans,answer)
        memo[key]=answer
        return memo[key]

s=Solution()
nums=[2,3,4,5]
print(s.jump(nums))
