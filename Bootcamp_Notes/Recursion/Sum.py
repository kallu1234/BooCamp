def Sum(arr):
    if len(arr)==0 :
        return 0
    
    sum=arr[0]+Sum(arr[1:])
    return sum

arr=[1,2,3,4]
ans=Sum(arr)
print(ans)