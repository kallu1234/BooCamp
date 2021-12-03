#Print the Data of given position...

def position(head,pos):
    count=0
    curr=head
    if count<pos:     
        while curr is not None:
            count=count+1
            if(count==pos):
                print("Data present at that position",str(curr.data))
                print("Position is",pos)
                
                break
            curr=curr.next
