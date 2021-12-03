class Solution:
    def rob(self, nums: List[int]) -> int:
        #if length of nums is 0 return 0
        if len(nums)==0:
            return 0
         #if len of nums if 1 return nums[1]
        if len(nums)==1:
            return nums[0]
        #if len of nums is 2 then max(nums[0],nums[1])
        if len(nums)==2:
            return max(nums[0],nums[1])
       
        n=nums.copy()
        n.pop()
        f1= self.Robbery(n,0,{})   #currIndex 0 se start he and rob hora he
        f2= self.Robbery(nums,1,{})  # if currIndex 0 se start he and not able to rob 
        return max(f1,f2)
        
    def Robbery(self,nums,currIndex,memo):
        
        if(currIndex>=len(nums)):
            return 0
        
        
        currKey=currIndex
        #tc->On(n)
        #sp->O(n)+O(n)->O(n)
        if currKey in memo:
            return memo[currKey]
        
            
        rob=nums[currIndex]+self.Robbery(nums,currIndex+2,memo)
        norob=self.Robbery(nums,currIndex+1,memo)
        
        memo[currKey]=max(rob,norob)
        return memo[currKey]
  
  
  
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
