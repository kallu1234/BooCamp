from math import sqrt,floor
memo={}
class Solution:
    def numSquares(self, n):
        # if n<=3:
        #     return n
        # else:
        s=floor(sqrt(n+1))
        nums=[x**2 for x in range(1,s+1)]
       
        
        return self.find(nums,0,n)
     
    def find(self,nums,currIndex,target):
        if currIndex>=len(nums) and target!=0:
            return 1000
        if target==0:
            return 0
        consider=10000
        key=(currIndex,target)
        if key in memo:
            return memo[key]
        
        # if currIndex==0 and nums[currIndex+1]>target:
        #     consider=1000
        
        if nums[currIndex]<=target:
            consider=1+self.find(nums,currIndex,target-nums[currIndex])
        notconsider=self.find(nums,currIndex+1,target)
        memo[key]=min(consider,notconsider)
        return memo[key]
        
        
    
        
s=Solution()
n=12
ans=s.numSquares(n)
print(ans)
