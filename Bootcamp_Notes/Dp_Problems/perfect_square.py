class Solution:
    def numSquares(self, n):
        perfect=[]
        for i in range(1,n+1):
            perfect.append(i*i)
        return self.LeastNum(0,n,perfect,{})               
        
    def LeastNum(self,currIndex,target,perfect,memo):
        if target==0:
            return 0
        if currIndex>=len(perfect):
                return 1000
            
        key=str(currIndex)+"->"+str(target)
        if key in memo:
            return memo[key]
        consider=1000
        
        if perfect[currIndex]<=target:
            
            consider=1+self.LeastNum(currIndex,target-perfect[currIndex],perfect,memo)
        notconsider=self.LeastNum(currIndex+1,target,perfect,memo)
        memo[key]= min(consider,notconsider)
        return memo[key]


n=int(input("Enter a value"))
s=Solution()
ans=s.numSquares(n)
print(ans)
