def ReplaceChar(str,a,b):
    if len(str)==0:
        return str
    
    smallOutput=ReplaceChar(str[1:],a,b)
    if str[0]==a:
        return b+smallOutput
    else:
        return str[0]+smallOutput


str=input("Enter a string:")
char=input("ENter a character ")
rep=input("ENter replace char:")
ans=ReplaceChar(str,char,rep)
print(ans)