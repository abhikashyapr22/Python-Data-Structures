class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

def reverse(head):
    current =head
    prev = None
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    
    head = prev
    
    return head
