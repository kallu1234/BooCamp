class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,capacity, weight, value, n):
       
        # code here
        
        return self.MaxProfit(capacity,weight,value,n,0,{})
        
    def MaxProfit(self,capacity,weight,value,n,currItem,memo):
        #if currItem is less than size of an weight array
        if currItem>=n:
            return 0
            
            
        key=str(currItem)+ "->" +str(capacity)
        if key in memo:
            return memo[key]
            
        consider=0
        if weight[currItem]<=capacity:
            consider=value[currItem]+self.MaxProfit(capacity-weight[currItem],weight,value,n,currItem+1,memo)
        
        notconsider=self.MaxProfit(capacity,weight,value,n,currItem+1,memo)
        
        
        
        memo[key]=max(consider,notconsider)
        return memo[key]


n=3
w=4
values=[1,2,3]
weight=[4,5,1]
s=Solution()
ans=s.knapSack(w,weight,values,n)
print(ans)
