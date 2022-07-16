class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
def deleteNode(head, position):
    temp = head
    prev = None
    for i in range(position):
        prev = temp
        temp = temp.next
    
    if prev is None:
        return temp.next
    prev.next = temp.next  
    return head
