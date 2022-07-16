class Node(object):
    
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def insertNodeAtTail(head, data):
  
    if head is None:
        head = Node(data)
        head.next = None
        
    else:
        temp = head
        while temp.next:
            temp = temp.next
       
        temp.next = Node(data)
    
    return head
