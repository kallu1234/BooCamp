def Binary_Search(a,x,si,ei):
    if si>ei:
        return -1
    
    mid=(si+ei)//2
    if a[mid]==x:
        return mid 
    elif a[mid]>x:
        return Binary_Search(a,x,si,mid-1)
    else:
        return Binary_Search(a,x,mid+1,ei)

arr=[1,2,3,4,5]
x=4
ans=Binary_Search(arr,x,0,len(arr)-1)
print(ans)
