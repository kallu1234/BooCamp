def Remove_X(str):
    if len(str)==0:
        return str
    
    
    smallOutput=Remove_X(str[1:])
    if str[0]=='x':
        return ''+smallOutput
    else:
        return str[0]+smallOutput

    return smallOutput

str=input("Enter a string:")
ans=Remove_X(str)
print(ans)