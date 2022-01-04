def Geometric_Sum(k):
    if k==0:
        return 1
    a=Geometric_Sum(k-1)
    ans=a+(1//2**k)
    return ans

ans=Geometric_Sum(5)
print(ans)
