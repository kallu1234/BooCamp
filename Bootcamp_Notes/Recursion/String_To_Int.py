def String_To_Int(str):
    #If length of string becomes 1 then find its int value
    if len(str)==1:
        #string present at 0th pos find its ascii and substract it  by ascii of '0' string
        return ord(str[0])-ord('0')
    pow=10**(len(str)-1)
    x=ord(str[0])-ord('0')
    ans=x*pow+String_To_Int(str[1:])
    return ans

a=input("Enter a value:")
ans=String_To_Int(a)
print(ans)