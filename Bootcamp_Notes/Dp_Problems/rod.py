class Solution:
    def cutRod(self, price, n):
        #code here
        return self.Rod(price,0,n,{})
   
   
    def Rod(self,price,currIndex,lenRod,memo):
        if lenRod==0:
            return 0
        if currIndex>=lenRod:
            return 0
        
        key=str(currIndex+1)+"->"+str(lenRod)
        #time complexity ->O(n)+O(7)->O(n)
        #space ->O(n)
        if key in memo:
            return memo[key]
        consider=0
        if currIndex<len(price):
            consider=price[currIndex]+self.Rod(price,currIndex,lenRod-(currIndex+1),memo)
        notconsider=self.Rod(price,currIndex+1,lenRod,memo)
        memo[key]=max(consider,notconsider)
        return memo[key]
s=Solution()
n=8
prices=[1,5,8,9,10,17,17,20]

ans=s.cutRod(prices,n)
print(ans)
