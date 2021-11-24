#here no need to consider transaction we can do no of transaction
class Solution:
    def maxProfit(self, prices):
        return self.BuySell(prices,0,1,{})#here 1 for True canBuy
    def BuySell(self,prices,currDay,canBuy,memo):
        if currDay>=len(prices):
            return 0
        
        key=(currDay,canBuy)
        #Time complexity->O(n)+O(2)-->O(n)
        #space complexity-->O(n)+O(n)-->O(2n)  ->O(n)
        
        
        if key in memo:
            return memo[key]
        idle=self.BuySell(prices,currDay+1,canBuy,memo)
        if (canBuy):
            # idle=self.BuySell(prices,currDay+1,canBuy,transaction,memo)
            buy=-prices[currDay]+self.BuySell(prices,currDay+1,0,memo)#here canBuy value changes to 0->False
            memo[key]=max(idle,buy)
           
        else:
            # idle=self.BuySell(prices,currDay+1,canBuy,transaction,memo)
            sell=prices[currDay]+self.BuySell(prices,currDay+1,1,memo)#Here canBuy regains to Treu bcoz transaction can be done no of times
            memo[key]=max(idle,sell)
        return memo[key]
            
            
        
        
s=Solution()
prices=[7,1,5,3,6,4]
ans=s.maxProfit(prices)
print(ans)
      
        
