def Find(arr,x):
    if len(arr)==0:
        return False
    if arr[0]==x:
        return True
    
    smallOutput=Find(arr[1:],x)
    return smallOutput

arr=[1,2,3,4,5,6]
x=int(input("Enter value to find:"))
ans=Find(arr,x)
print(ans)