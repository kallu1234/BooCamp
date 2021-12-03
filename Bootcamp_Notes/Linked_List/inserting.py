#Inserting data At any givene position 

def inserting(head,pos,data):
  
    #check if pos is less than 0  or greater than the length given 
    if pos<0 or pos> length(head):
        return head
      
      
    count=0
    prev=None
    curr=head
    
    #  iterate till pos count < given pos  
    while count<pos:
        prev=curr
        curr=head.next 
        
    # create a new Node 
    newNode=Node(data)
    
    if prev is not None:
        prev.next=newNode
        newNode.next=curr
    else:
        head=newNode
        newNode.next=curr
    printL(head)
    return head   

