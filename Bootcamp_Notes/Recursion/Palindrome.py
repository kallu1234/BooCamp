def Palindrome(s,si,ei):
    if si>=ei:
        return s
    if s[si]==s[ei]:
        return True
    else:
        return False
    smallOutput=Palindrome(s[si+1,ei-1],si,ei)
    return smallOutput
#using Recursion it takes O(n) time and O(n) space for stack 
def Palindrome_Iteative(str):
    i=0
    j=len(str)-1
    while(i<=j):
        if str[i]!=str[j]:
            return False
    return True 
#it takes O(n) times and space is O(1)
str=input("Enter a string:")
ans=Palindrome(str,0,len(str)-1)
print(ans)