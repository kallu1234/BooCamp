class Solution:
    def tribonacci(self, n):
        return self.nthFibo(n,{})
    def nthFibo(self,n,memo):
        if n<=1:
            return n
        if n==2:
            return 1
        
        currKey=n
        if currKey in memo:
            return memo[currKey]
        
        a=self.nthFibo(n-1,memo)
        b=self.nthFibo(n-2,memo)
        c=self.nthFibo(n-3,memo)
        
        memo[currKey]=a+b+c
        return memo[currKey]
        
        

s=Solution()
n=input("Enter n->")
ans=s.tribonacci(n)
print(ans)
