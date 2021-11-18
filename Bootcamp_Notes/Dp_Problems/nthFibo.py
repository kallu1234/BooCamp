class Solution:
    def fib(self, n):
        return self.nFibo(n,{})
    
    def nFibo(self,n,memo):
        if n<=1:
            return n
        currKey=n
        if currKey in memo:
            return memo[currKey]
        
        a=self.nFibo(n-1,memo)
        b=self.nFibo(n-2,memo)
        
        memo[currKey]=a+b
        return memo[currKey]
        
        
        
s=Solution()
n=input("Enter n->")
ans=s.fib(n)
print(ans)
