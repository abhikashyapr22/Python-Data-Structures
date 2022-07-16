class Node:
    def __init__(self):
        self.data = data
        self.next = next

def getNode(head, positionFromTail):
    count = 0
    temp = head
    while temp:
        temp = temp.next
        count += 1
    
    temp1 = head
    pos = count - positionFromTail
    for i in range(1,pos):
        temp1 = temp1.next
        
    return temp1.data
