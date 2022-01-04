from Recursion.Find_X import Find


def Sorted(arr):
    if len(arr)==0 or len(arr)==1:
        return True 
    
    else:
        if arr[0]>arr[1]:
            return False
        smalloutput=Sorted(arr[1:])
    return smalloutput

def isSorted(arr,si):
    l=len(arr)
    if si==l-1 or si==1:
        return True
    if arr[si]>arr[si+1]:
        return False
    isSmallSorted=isSorted(arr,si+1)
    return isSmallSorted
arr=[1,2,30,4]
ans=Sorted(arr)
print(ans)