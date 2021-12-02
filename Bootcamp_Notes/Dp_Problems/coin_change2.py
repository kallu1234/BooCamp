class Solution:
   #using unbounded kanpsack
    def change(self, amount: int, coins: List[int]) -> int:
          #curentIndex start from 0 
          return self.TotalWays(coins,0,amount,{}) 
       
    def TotalWays(self,coins,currentindex,amount,memo): 
       #base condition if amount ==0 return 1 bcoz here we have to find how many ways to calculate the given amount
        if(amount==0): 
            return 1 
          
         #if curretnIndex is greater than lenght ofcoins return 0
        if(currentindex>=len(coins)): 
             return 0
          
         # create key to amintain subproblems in dp
        currentkey=str(currentindex)+"_"+str(amount) 
        
        #see if key is in memo
        if currentkey in memo: 
            return memo[currentkey] 
          
        #here consider is decleared as 0 
        consider=0
        if(coins[currentindex]<=amount): 
            #current index remains same bcoz unbounded kanpsack is used
            consider=self.TotalWays(coins,currentindex,amount-coins[currentindex],memo) 
        notconsider=self.TotalWays(coins,currentindex+1,amount,memo) 
        memo[currentkey]=consider+notconsider
        return memo[currentkey]
      
      
# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
