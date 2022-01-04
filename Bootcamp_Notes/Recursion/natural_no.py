def Natural(n):
    #base condition 
    if n==0:
        return 
    
    print(n )#we print n n-1 n-2 .....1

    Natural(n-1)#recursion to print n-1 
    
    print(n) # print from 1 to n 

a=int(input("enter val:"))
ans=Natural(a)    
