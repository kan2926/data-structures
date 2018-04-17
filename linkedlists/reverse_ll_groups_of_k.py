import sys
from linked_list_prototype import ListNode
import math

def reverse_list(self):
        prev = None
        current = self
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self = prev
        return self
    
def reverse(head, k):
        current = head 
        next  = None
        prev = None
        count = 0
         
        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
 
        if next is not None:
            head.next = reverse(next, k)
 
        # prev is new head of the input list
        return prev
        
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
k = int(input('Enter no. of groups k: '))
print_list(reverse(L1,k))
