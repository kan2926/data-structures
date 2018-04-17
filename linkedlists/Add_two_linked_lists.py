from linked_list_prototype import ListNode

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
def getcnt(a):
    cnt = 0
    while a:
        cnt += 1
        a = a.next
    return cnt

def padzeros_to_list(a, actual, req):
    curr = a
    zeronode = ListNode()
    while req > 0:
        zeronode.data = 0
        zeronode.next = a
        req -= 1
        padzeros_to_list(zeronode, actual, req)
    return zeronode
    
def add_two_lists(a1, a2):
    m = getcnt(a1)
    n = getcnt(a2)
    if m < n:
        a1 = padzeros_to_list(a1, m, n-m)
    else:
        a2 = padzeros_to_list(a2, n, m-n)
    res = add_lists(a1,a2, 0)
    return res
        
def add_lists(a1, a2, carry):
    result = ListNode()

    if a1 is None and a2 is None and carry == 0:
        return None
 
    value = carry
    if a1 != None:
        value += a1.data
    if a2 != None:
        value += a2.data

    result.data = value%10
    if  value >= 10:
        value = 1
    else:
        value = 0
    if a1.next != None and  a2.next != None:
        more = add_lists(a1.next, a2.next, value)
        result.next = more
        
    if a1.next is None and a2.next is None and value > 0:
        additional_node = ListNode()
        additional_node.data = value
        additional_node.next = None
        result.next = additional_node
        return result

    return result
    

    
L6 = ListNode(6,None)
L5 = ListNode(2,L6)
L4 = ListNode(4,L5)
L3 = ListNode(4,None)
L2 = ListNode(2,L3)
L1 =ListNode(1,L2)
#print("List 1: ")
#print_list(L1)
#print("List 2 :")
#print_list(L4)
#result = add_two_lists(L1, L4)
#print('result ---')
#print_list(result)
P11 = ListNode(2, None)
P1 = ListNode(1, P11)
P2 = ListNode(0, None)
P3 = add_two_lists(P1, P2)
print_list(P3)
