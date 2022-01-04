def Find_Last_Index(arr,x):
    if len(arr)==0:
        return -1
    smallOutput=Find_Last_Index(arr[1:],x)
    if smallOutput!=-1:
        return smallOutput+1
    else:
        if arr[0]==x:
                return 0
        else:
                return -1


   
arr=[1,5,3,4,5]
x=5
ans=Find_Last_Index(arr,x)
print(ans)