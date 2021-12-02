class Solution: 
   
    def coinChange(self, coins: List[int], amount: int) -> int: 
        
        ans= self.mincoins(coins,0,amount,{}) 
        if(ans==100000): 
            return -1 
        else: 
            return ans 
    def mincoins(self,coins,currentindex,amount,memo): 
        #base case if amt is 0 then return 0
        if(amount==0): 
            return 0 
          
        #base condiiton if currIndex is greater than the lenght of coins given
        if(currentindex>=len(coins)): 
             return 100000
          
         #create a key to optimize
        currentkey=str(currentindex)+"_"+str(amount) 
        
        #check if key is present of not in memo (dictionary)
        if currentkey in memo: 
            return memo[currentkey] 
          
        # here i considered value as 10000 bcoz we have to find the min amount to calculate the ans=min(consider,notconsider)
        consider=100000 
        
        #if currenIndex in coins<=amount then only consider than value else no need
        if(coins[currentindex]<=amount): 
            #now we considered that index value  and add 1+ to calculate how many no's are required to achive that target value
            consider=1+self.mincoins(coins,currentindex,amount-coins[currentindex],memo) 
            
        #if that value is not considered we simply increase that value    
        notconsider=self.mincoins(coins,currentindex+1,amount,memo) 
        
        #find the min of considered value and notconsidered 
        memo[currentkey]=min(consider,notconsider) 
        return memo[currentkey]
      
      
    #using unbunded knapsack 
    #coins = [1,2,5], amount = 11 
    #so how we can get 11 as amount 
    #5+5+1->11  
    #1+1+1+1+1+1+1+1+1+1+1=  11 
    #but here we have to find min ways to get that amout
