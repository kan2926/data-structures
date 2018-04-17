
import sys
import os

class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None

def _insert_node_into_singlylinkedlist(head, tail, val):
    if head == None:
        head = LinkedListNode(val)
        tail = head
    else:
        node = LinkedListNode(val)
        tail.next = node
        tail = tail.next
    return tail

def get_cnt(l):
    if l is None:
        return None
    cnt = 0
    tmp = l
    while tmp.next != l:
        cnt += 1
        tmp = tmp.next
    return cnt

import math
def find_median(ptr):
    size = get_cnt(ptr)+1
    print('size of the list: ',size)
    curr = ptr
    trv_node_cnt = math.ceil(size/2)
    odd = False
    if size%2 == 1:
        print('no. of nodes to traverse:',trv_node_cnt)
        odd = True
    i= 0
    curr = ptr
    median = 0
    if odd :
        while i <= trv_node_cnt:
            curr = curr.next
            i += 1
        curr = curr.next.next
        median = curr.val
    else:
        while i <= trv_node_cnt+1:
            curr = curr.next
            i += 1
        next_node = curr.next.next
        print(curr.next.val , ' + ', next_node.val)
        median = int((curr.next.val + next_node.val)/2)
    return median

def find_median_of_nodes(ptr):
    
    slow = fast = ptr
    if ptr is None:
        return None
    while fast != ptr and fast.next != ptr:
        fast = fast.next.next
        slow = slow.next
    return slow


if __name__ == "__main__":
    ptr = None
    ptr_tail = None
    ptr_size = int(input('size:'))
    ptr_i = 0
    while ptr_i < ptr_size:
        ptr_item = int(input('enter nodes:'))

        ptr_tail = _insert_node_into_singlylinkedlist(ptr, ptr_tail, ptr_item)
        if ptr_i == 0:
            ptr = ptr_tail
        ptr_i += 1

    #----added manually----
    ptr_tail.next = ptr
    arbitrary_shift = int(input('provide input to circular linked list:'))
    while (arbitrary_shift > 0):
        arbitrary_shift -= 1
        ptr = ptr.next
    #--------

    middle_node = find_median_of_nodes(ptr)
    print(middle_node.val)
    res = find_median(ptr)
    print(res)

    

    
