class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

def insertNodeAtHead(llist, data):

    if llist:
        return Node(data,llist)
    
    return Node(data)
