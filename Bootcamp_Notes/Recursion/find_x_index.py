def Find_X(arr,x):
        if len(arr)==0:
            return -1
        if arr[0]==x:
            return 0
        smallOutput=1+Find_X(arr[1:],x)
        return smallOutput
def Find(arr,si,x):
    l=len(arr)
    if si==l:
        return -1
    if arr[si]==x:
        return si
    smallOutput=1+Find(arr[1:],si+1,x)
    return smallOutput

arr=[1,2,3,4,5]
x=5
ans=Find(arr,0,x)
print(ans)