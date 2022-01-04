def Power(a,b):
    if a ==0:
        return 0
    if b ==0:
        return 1
    smallOutput=Power(a,b-1)
    output=a*smallOutput
    return output

a=int(input("Enter no"))
b=int(input("Enter power:"))
ans=Power(a,b)
print(ans)