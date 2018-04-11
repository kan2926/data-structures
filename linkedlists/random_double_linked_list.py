from double_linked_List_prototype import DoubleListNode
from collections import deque
def print_double_linked_list_forward(head):
    nodes = deque()
    while head:
        nodes.append(head.data)
        head = head.next

    while nodes:
        print(nodes.popleft())

def print_double_linked_list_backward(head):
    while head.next != None: 
        head = head.next
    while head != None:
        print(head.data)
        head = head.prev

def create_node_in_between(head):
    curr = head
    while curr:
        temp = curr.next
        curr.next = DoubleListNode(curr.data+10)
        curr.next.next = temp
        curr = temp

def random_pointers_clone(head):
    curr = head
    create_node_in_between(head)
 
    while curr != None:
        curr.next.prev = curr.prev.next 
        curr = curr.next.next
    original = head
    copy =head.next
    temp = copy
    while original and copy:
        original.next = original.next.next
        if copy.next != None:
            copy.next = copy.next.next
        original = original.next
        copy = copy.next
    return temp

def _insert_node_into_doublylinkedlist(head, tail, val):
    if head == None:
        head = DoubleListNode(val, prev_node = None) 
        tail = head
    else:
        node = DoubleListNode(val)
        tail.next = node
        node.prev = tail
        tail = tail.next
    return tail

def create_random_pointers(a):
    this_node = a
    while this_node.next != None :
        print(this_node.prev,'----',this_node.next.next)
        this_node.prev = this_node.next.next
        this_node = this_node.next
        print(this_node.data)
    return a

def main():
    P5 = DoubleListNode(5, None, None)
    P4 = DoubleListNode(4, P5, None)    
    P3 = DoubleListNode(3, P4, None)
    P2 =  DoubleListNode(2, P3, None)
    P1 =  DoubleListNode(1, P2, None)
    P1.prev = P3
    P4.prev = P1
    P5.prev = P3
    P2.prev = P1
    P3.prev = P5
    
    #a = create_random_pointers(_pList)    
    print_double_linked_list_forward(P1)
    B1 = random_pointers_clone(P1)
    print_double_linked_list_forward(B1)
 
if __name__ == '__main__':
    main()
