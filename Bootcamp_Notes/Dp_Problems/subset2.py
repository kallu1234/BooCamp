
class Solution:
    def canPartition(self, nums,diff):
        
        total=sum(nums)
        total1=total-diff
        if total1%2!=0:
            return False
        return self.isPossible(nums,0,total1//2,len(nums),{})
    
    def isPossible(self,nums,currIndex,targetSum,n,memo):
        if targetSum==0:
            return True
        if currIndex>=n:
            return False
        
        
        key=str(currIndex) +"->"+ str(targetSum)
        if key in memo:
            return memo[key]
        
        consider=False
        if nums[currIndex]<=targetSum:
            consider=self.isPossible(nums,currIndex+1,targetSum-nums[currIndex],n,memo)
        
        
        
        notconsider=self.isPossible(nums,currIndex+1,targetSum,n,memo)
        
        memo[key]=consider or notconsider
        
        return memo[key]
        
        
s=Solution()
nums=[1,2,2,2,2]
diff=3
ans=s.canPartition(nums,diff)
print(ans)
