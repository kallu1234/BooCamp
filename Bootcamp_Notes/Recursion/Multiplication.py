def Multiplication(a,b):
    if b==0:
        return 0
    
    mul=a+Multiplication(a,b-1)
    return mul
a=3
b=5
ans=Multiplication(a,b)
print(ans)
