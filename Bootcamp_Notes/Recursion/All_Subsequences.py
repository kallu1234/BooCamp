def All_Subsequnces(s):
    if len(s)==0:
        output=[]
        output.append(" ")
        return output

    smallOutput=All_Subsequnces(s[1:])
    output=[]
    for sub in smallOutput:
        output.append(sub)
    for sub in smallOutput:
        output.append(s[0]+sub)
    return output

str=input("Enter string:")
ans=All_Subsequnces(str)
print(ans)