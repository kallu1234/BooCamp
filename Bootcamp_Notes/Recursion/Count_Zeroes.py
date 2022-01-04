from typing import Counter


def Count_Zeroes(n):
    #if n becomes zero then reurn 0
    if n==0:
        return 0
    #if n %10 is zero then cont htat value
    if n%10==0 :
        return 1+Count_Zeroes(n//10)
    else:#else this no is not zero so as it is n//10
        return Count_Zeroes(n//10)

n=int(input("Enter val:"))
ans=Count_Zeroes(n)
print(ans)