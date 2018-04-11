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

def main():
    P3 = DoubleListNode(44,None,None)
    P2 = DoubleListNode(33,P3,None)
    P1 = DoubleListNode(22,P2,None)
    P3.prev = P2
    P2.prev = P1
    print('Forward double linked list print---')
    print_double_linked_list_forward(P1)
    print('Reverse double linked list print---')
    print_double_linked_list_backward(P1)


if __name__ == '__main__':
    main()
