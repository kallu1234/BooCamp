def Quick(arr,si,ei):
    if si>=ei:
        return
    pivot_index=Partition(arr,si,ei)
    left=Quick(arr,si,pivot_index-1)
    right=Quick(arr,pivot_index+1,ei)

    return arr

def Partition(arr,si,ei):
    pivot=arr[si]
    count=0
    for i in range(si,ei+1):
        if arr[i]<pivot:
            count+=1
    #swap 
    arr[si+count],arr[si]=arr[si],arr[si+count]
    pivot_index=si+count

    i=si 
    j=ei
    while i<j:
        if  arr[i]<pivot:
            i=i+1
        elif arr[j]>=pivot:
            j=j-1
        else:
            arr[i],arr[j]=arr[j],arr[i]
            i=i+1
            j==j-1
    return pivot_index

arr=eval(input("Enter an aray: "))
ans=Quick(arr,0,len(arr)-1)
print(ans)