import sys
import random
from linked_list_prototype import ListNode
#from reverse_linked_list_iterative import reverse_linked_list

def reverse_print_list(self):
        prev = None
        current = self
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self = prev
        return self

def pairwiseswap(self):
    curr = self
    prev = None
    if curr != None and curr.next != None:
        tmp = curr.data
        curr.data = curr.next.data
        curr.next.data = tmp
        pairwiseswap(curr.next.next)
    return self

def print_list(head):
    while head != None:
        print(head.data)
        head = head.next
L7 = ListNode(7,None)
L6 = ListNode(6,L7)
L5 = ListNode(5,L6)
L4 = ListNode(4,L5)
L3 = ListNode(3,L4)
L2 = ListNode(2,L3)
L1 =ListNode(1,L2)
print_list(L1)
P1 = pairwiseswap(L1)
print_list(P1)
