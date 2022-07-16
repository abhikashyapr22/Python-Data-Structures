class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

def insertNodeAtPosition(head, data, position):
    temp = head
    for i in range(1,position):
        temp = temp.next
        n += 1
        
    new_data = Node(data)
    new_data.next = temp.next 
    temp.next = new_data    
        
    return head
