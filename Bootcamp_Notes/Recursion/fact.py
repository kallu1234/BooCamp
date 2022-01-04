#factorial using recursion
def Factorial(n):
    #Base case
    if n ==0 or n==1:
        return n
    fact=n*Factorial(n-1)
    return fact

n=int(input())
ans=Factorial(n)
print(ans)
#Bydefault python has recursion depth of 1000

#Maths behind recursion
#PMI->principle of mathematics induction
#we have to prove f statement is true for all natural numbers for eaxmple

#Task1: f(0),f(1) is true
# so lets say 1=1(1+1)/2  (by using formula n*(n+1)/2)
# so here we get 1==1 LHS==RHS for smaller input we get LHS=RHS

#Assume f(k) is true

#Task2:f(k+1) is true
#so lets say (k+1)=(k+1)(k+1+1)/2 by formula of summation

#we know k=k*(k+1)/2 is true
# so k+1=sum of k + k+1
#sum of k+1= sum of k + k+1

