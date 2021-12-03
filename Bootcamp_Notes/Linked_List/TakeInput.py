def takeinput():
   #for taking input i used list comprehension
    inputList=[int(ele) for ele in input().split()]
    
    #head and tail i denoted as null 
    head=None
    tail=None
    
    #whatever input we gave check wheather it is -1 if (-1) then break
    for currData in inputList:
        if currData==-1:
            break
        #we create a new node 
        newNode=Node(currData)
        
        #check if head is None
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
#             curr =head
#             while curr.next is not None:
#                 curr=curr.next
#             curr.next=newNode
    return head
