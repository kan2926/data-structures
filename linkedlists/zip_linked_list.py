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


def zip_list(L):
        if not L or not L.next:
                return L

        # Finds the second half of L.
        slow = fast = L
        while fast and fast.next:
                slow, fast = slow.next, fast.next.next
        first_half_head = L
        second_half_head = slow.next
        slow.next = None  # Splits the list into two lists.
 
        second_half_head = reverse_print_list(second_half_head)
        first_half_iter, second_half_iter = first_half_head, second_half_head
        while second_half_iter!= None:
                second_half_iter.next, first_half_iter.next, second_half_iter = (first_half_iter.next, second_half_iter, second_half_iter.next)
                first_half_iter = first_half_iter.next.next
        return first_half_head

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
#zipping_linked_list(L1)
#print_list(L1)
zip_head = zip_list(L1)
print_list(zip_head)
