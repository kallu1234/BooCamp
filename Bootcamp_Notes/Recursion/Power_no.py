def Power_of_no_Present(no):
    if no==1:
        return True
    if no%2!=0 or no<=0:
        return False


    smallOutput=Power_of_no_Present(no//2)
    return smallOutput
def Power_of_no(no):#If i say 2^4->16 so value is 4
    if no==0:
        return 1
    if no%2!=0 or no<=0:
        return False


    smallOutput=1+Power_of_no(no//2)
   
    return smallOutput


ans=Power_of_no(16)
print(ans)