def Sum(n):
    #if n is 0 then sum will be 0 only
    if n==0:
        return 0
    smallOutput=Sum(n-1)
    output=n+smallOutput
    return output
    # sum=n+Sum(n-1) #smalloutput is Sum(n-1)
    # return sum

n=int(input())
ans=Sum(n)
print(ans)