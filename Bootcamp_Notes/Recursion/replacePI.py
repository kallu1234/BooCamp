def Replace_PI(str):
    if len(str)==0 or len(str)==1:
        return str 
    
    smallOutput=Replace_PI(str[2:])
    if str[0]=='p' and str[1]=='i':
        return "3.14"+smallOutput
    else:
        smallOutput=Replace_PI(str[1:])
        return str[0]+smallOutput
            
        
str="piabcpi"
ans=Replace_PI(str)
print(ans)