class Node:
    def __init__(self,data=0, next=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        this_node = self.head
        while this_node:
            print(this_node.data)
            this_node = this_node.next

    def append(self, new_data):
        this_node = self.head        
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        while this_node.next:
            this_node = this_node.next
        this_node.next = new_node

def mergelists(a,b):
    merged_list = LinkedList()
    tail = Node()
    l1 = a.head
    l2 = b.head
    while l1 and l2:
        if l1.data < l2.data:
            tail, l1 = l1, l1.next
        else:
            tail, l2 = l2, l2.next
        merged_list.append(tail.data)
        tail = tail.next
    while l1:
        tail = l1
        merged_list.append(tail.data)
        l1 = l1.next
    while l2:
        tail= l2
        merged_list.append(tail.data)
        l2 = l2.next
        
    return merged_list
    
if __name__ == '__main__':
    a = LinkedList()
    a.append(4)
    a.append(6)
    a.append(9)
    print('List A')
    a.print_list()

    b = LinkedList()
    b.append(1)
    b.append(5)
    b.append(10)
    b.append(20)
    b.append(30)
    print('List B')
    b.print_list()

    c = mergelists(a,b)
    print('Merged List')
    c.print_list()
        
