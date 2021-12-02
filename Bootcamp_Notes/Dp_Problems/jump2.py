class Solution:
    def jump(self, nums):
        #to find minimum no of jums
        return self.minJumps(nums,0,{})
    
    def minJumps(self,nums,currIndex,memo):
#         if currentIndex is greater than length of nums given
        if currIndex>=len(nums)-1:
            return 0
        
        
#         find minimum of jumps to reah final index 
        answer=10000
    
        key=currIndex
        if key in memo:
            return memo[key]
        
#         currentJump of currIndex 
        currJump=nums[currIndex]
#     itterate through array to find the final destination
        for i in range(1,currJump+1):
        
            ans=1+self.minJumps(nums,currIndex+i,memo)
            answer=min(ans,answer)
        memo[key]=answer
        return memo[key]

s=Solution()
nums=[2,3,4,5]
print(s.jump(nums))


# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index
