class Solution:
    def minCut(self, s: str) -> int:
        memo={}
        if len(s)==1:
            return 0
        if len(s)==2:
            if s[0]==s[1]:
                return 0
            else:
                return 1
       
        return self.MinCut(s,0,len(s)-1,memo)
    def MinCut(self,s,start,end,memo):
        if self.isPalindrome(s,start,end) is True or start==end:
            return 0
        
        key=(start,end)
        if key in memo:
            return memo[key]
        
        ans=1000
        
        for currentCut in range(start,end):
            if self.isPalindrome(s,start,currentCut):
            # leftHalf=self.MinCut(s,start,currentCut,memo)
                rightHalf=self.MinCut(s,currentCut+1,end,memo)
                tempans=1+rightHalf
                ans=min(ans,tempans)
       
        memo[key]=ans
        return memo[key]
            
        
        
        
    def isPalindrome(self,s,start,end):
        while start<=end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True
    
        
            
            
