
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


def getcnt(a):
    cnt = 0
    while a:
        cnt += 1
        a = a.next
    return cnt

def padzeros_to_list(a, actual, req):
    zeronode = LinkedListNode(0)
    if req > 0:
        zeronode.next  = a
    return zeronode


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
    
def addNumbers(a1, a2):
    m = getcnt(a1)
    n = getcnt(a2)
    if n == 0:
        return a1
    elif m == 0:
        return a2
    elif m < n:
        a1 = padzeros_to_list(a1, m, n-m)
        while m < n:
            a1 = padzeros_to_list(a1, m, n-m)
            m+=1
        a1 = reverse_list(a1)
    elif m > n:
        while m > n:
            a2 = padzeros_to_list(a2, n, m-n)
            n+=1
        a2 = reverse_list(a2)
    res = add_lists(a1,a2, 0)
    return res
        
def add_lists(a1, a2, carry):
    result = LinkedListNode(0)
    tmp = a1
    
    if a1 is None and a2 is None and carry == 0:
        return None
    value = carry
    if a1 != None:
        value += a1.val
    if a2 != None:
        value += a2.val
        
    result.val = value%10
    
    if  value >= 10:
        value = 1
    else:
        value = 0
        
    if a1.next != None and  a2.next != None:
        more = add_lists(a1.next, a2.next, value)
        result.next = more
        
    if a1.next is None and a2.next is None and value > 0:
        additional_node = LinkedListNode(0)
        additional_node.val = value
        additional_node.next = None
        result.next = additional_node
        return result
    return result


_l1 = None
_l1_tail = None
_l1_size = 0
_l1_size = int(input())
_l1_i=0
while _l1_i < _l1_size:
    _l1_item = int(input());
    if _l1_i == 0:
        _l1 = _insert_node_into_singlylinkedlist(_l1, _l1_tail, _l1_item)
        _l1_tail = _l1
    else:
        _l1_tail = _insert_node_into_singlylinkedlist(_l1, _l1_tail, _l1_item)
    _l1_i += 1


_l2 = None
_l2_tail = None
_l2_size = 0
_l2_size = int(input())
_l2_i=0
while _l2_i < _l2_size:
    _l2_item = int(input());
    if _l2_i == 0:
        _l2 = _insert_node_into_singlylinkedlist(_l2, _l2_tail, _l2_item)
        _l2_tail = _l2
    else:
        _l2_tail = _insert_node_into_singlylinkedlist(_l2, _l2_tail, _l2_item)
    _l2_i += 1

a, b = _l1, _l2
print('list1 ')
while a!= None:
    print(str(a.val))
    a = a.next
print('list 2')
while b!= None:
    print(str(b.val))
    b = b.next
print('result list   ')
res = addNumbers(_l1, _l2)
while (res != None):
    print(str(res.val) + "\n")
    res = res.next
