#!/bin/python3
import math
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
def makelist(a):
        _pList = None
        _pList_tail = None
        _pList_size = 0
        #_pList_size = len(a)
        _pList_i=0
        for _pList_i in range(len(a)):
            _pList_item = a[_pList_i];
            if _pList_i == 0:
                _pList = _insert_node_into_singlylinkedlist(_pList, _pList_tail, _pList_item)
                _pList_tail = _pList
            else:
                _pList_tail = _insert_node_into_singlylinkedlist(_pList, _pList_tail, _pList_item)
        return _pList


def alternativeSplit(pList):
    odd = even = pList
    even = even.next
    o = []
    e = []
    
    while odd.next and even.next :
        o.append(odd.val)
        e.append(even.val)
        odd = even.next
        even = odd.next
    if odd != None:
        o.append(odd.val)
    if even != None:
        e.append(even.val)
    #pOdd = makelist(o)
    #pEven  = makelist(e)
    print(",".join(map(str,o)))
    print(",".join(map(str,e)))
    return None
    
_pList = None
_pList_tail = None
_pList_size = 0
_pList_size = int(input())
_pList_i=0
while _pList_i < _pList_size:
    _pList_item = int(input());
    if _pList_i == 0:
        _pList = _insert_node_into_singlylinkedlist(_pList, _pList_tail, _pList_item)
        _pList_tail = _pList
    else:
        _pList_tail = _insert_node_into_singlylinkedlist(_pList, _pList_tail, _pList_item)
    _pList_i += 1
##
##while _pList != None:
##    print(str(_pList.val))
##    _pList = _pList.next
##    
res = alternativeSplit(_pList);
#while (res != None):
#    f.write(str(res.val) + "\n")
#    res = res.next;
#f.close()

