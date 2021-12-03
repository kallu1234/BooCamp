#For counting number of nodes present in  the linked list 

def length(head):
    count=0
    while head is not None:
        count=count+1
        head=head.next 
    # print("\nthe no of nodes present",count)
    return count
