def Fibo(n):
    if n==1 :
        return 1
    if n==0:
        return 0
    
    fib1=Fibo(n-1)
    fib2=Fibo(n-2)

    output=fib1+fib2
    return output
   

a=int(input("ENter a val:"))
ans=Fibo(a)
print(ans)