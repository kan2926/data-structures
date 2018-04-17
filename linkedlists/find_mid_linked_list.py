from linked_list_prototype import ListNode

def print_list(head):
    while head != None:
        print(head.data)
        head = head.next

def find_mid(head):
    slow = fast = head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
    return slow

def rev_list(head):
    prev = None
    current = head
    while current != None:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    head = prev
    return head
    

L5=ListNode(5,None)
L4=ListNode(4,L5)
L3=ListNode(3,L4)
L2=ListNode(2,L3)
L1= ListNode(1,L2)
print_list(L1)
mid = find_mid(L1)
print('mid node:',mid.data)
L5=rev_list(L1)
print_list(L5)
