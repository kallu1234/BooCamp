def MergeSort(arr):
    if len(arr)==0 or len(arr)==1:
        return arr 
    
    mid=len(arr)//2
    a1=arr[0:mid]
    a2=arr[mid:]
    
    MergeSort(a1)
    MergeSort(a2)


    ans=Merge(a1,a2,arr)
    return ans 

def Merge(a1,a2,arr):
      i,j,k=0,0,0
      while i<len(a1) and j<len(a2):
          if a1[i]<a2[j]:
              arr[k]=a1[i]
              i+=1
              k+=1
          else:
              arr[k]=a2[j]
              j+=1
              k+=1

      while i<len(a1):
              arr[k]=a1[i]
              i+=1
              k+=1
      while j<len(a2):
          arr[k]=a2[j]
          j+=1
          k+=1
      return arr
          


arr=eval(input("Enter array:"))
ans=MergeSort(arr)
print(ans)