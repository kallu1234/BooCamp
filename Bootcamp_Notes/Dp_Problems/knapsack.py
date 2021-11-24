class Solution:
    def knapSack(self, N, cap, val, wt):
        # code here
        return self.MaxProfit(N,cap,val,wt,0,{})
    def MaxProfit(self,N,cap,val,wt,currIndex,memo):
        if currIndex>=n:
            return 0
            
        key=str(currIndex)+'->'+str(cap)
        if key in memo:
            return memo[key]
        consider=0
        if wt[currIndex]<=cap:
            consider=val[currIndex]+self.MaxProfit(N,cap-wt[currIndex],val,wt,currIndex,memo)
        notconsider=self.MaxProfit(N,cap,val,wt,currIndex+1,memo)
        
        memo[key]= max(consider,notconsider)
        return memo[key]
s=Solution()
n=2
cap=3
val=[1,1]
wt=[2,1]
ans=s.knapSack(n,cap,val,wt)
print(ans)
