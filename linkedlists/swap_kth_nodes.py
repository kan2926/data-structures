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

def print_list(head):
    while head != None:
        print(head.data)
        head = head.next
def swap(L, x, y):
    if x == y:
        return
    prevX = None
    currX = L
    while currX != None and currX != x:
        prevX = currX
        currX = currX.next
        
    prevY = None
    currY = L
    while currY != None and currY != y:
        prevY = currY
        currY = currY.next
    if currX == None or currY == None:
        return

    if prevX != None:
        prevX.next = currY
    else:
        L = currY

    if prevY != None:
        prevY.next = currX
    else:
        L = currX

    temp = currX.next
    currX.next = currY.next
    currY.next = temp
    print_list(L)
        

def swap_nodes(L1, k):
    if L1 == None :
        return
    if L1.next == None:
        return L1
    first = last = L1
    node_cnt = 1
    while last.next != None:
        node_cnt += 1
        last = last.next
    if k > node_cnt:
        return L1
    else:
        swap_head = swap_end=L1
        swap_head_iter = swap_end_iter = 1
        swap_head_prev = swap_end_prev = None
        while swap_end_iter <= (node_cnt-k):
            swap_end_prev = swap_end
            swap_end = swap_end.next
            swap_end_iter +=1
        while swap_head_iter <= k-1:
            swap_head_prev = swap_head
            swap_head = swap_head.next
            swap_head_iter +=1
        if swap_head == None or swap_end == None:
            return

        if swap_head_prev != None:
            swap_head_prev.next = swap_end
        else:
            L1 = swap_end

        if swap_end_prev != None:
            swap_end_prev.next = swap_head
        else:
            L1 = swap_head

        temp = swap_head.next
        swap_head.next = swap_end.next
        swap_end.next = temp
        return L1
    
    #swap(L1,swap_head, swap_end)


L7 = ListNode(7,None)
L6 = ListNode(6,L7)
L5 = ListNode(5,L6)
L4 = ListNode(4,L5)
L3 = ListNode(3,L4)
L2 = ListNode(2,L3)
L1 =ListNode(1,L2)
print_list(L1)
k = int(input('enter k: '))
print_list(swap_nodes(L1,k))

P2 = ListNode(-20, None)
P1 = ListNode(-10, P2)
k = int(input('enter k for second list: ' ))
print_list(swap_nodes(P1,k))
