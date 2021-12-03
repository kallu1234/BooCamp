
#This is a small Method by which i can increment the data of node
def increment(head):
   
    temp=head
    #itterate while temp is not None 
    while temp is not None:
        #increament the data present in that Node
        temp.data+=1
        temp=temp.next
    printL(head)
    
 #For printing that Linkd List 
 def printL(head):
        while head is not None:
            print(str(head.data)+'->',end='')
            head=head.next
