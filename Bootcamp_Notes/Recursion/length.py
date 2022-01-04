def Lenght(arr):
    if len(arr)==0:
        return 0
    # if arr==[]:
    #     return 0
    
    smallOutput=1+Lenght(arr[1:])
    return smallOutput
    #iterative is best bcoz it takes O(n) space for stack and tc->O(N)

arr=eval(input("Enter an aray: "))
ans=Lenght(arr)
print(ans)
