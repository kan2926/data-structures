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

def mergeSortList(pList):
    if pList == None or pList.next == None:
        return pList
    pList_left, pList_right = divide_list(pList)
    left = mergeSortList(pList_left)
    right = mergeSortList(pList_right)
    return mergelist(left, right)

def mergelist(pList_left, pList_right):
    merged_list = LinkedListNode(None)
    curr = merged_list
    while pList_left and pList_right:
        if pList_left.val < pList_right.val:
            curr.next = pList_left
            pList_left = pList_left.next
        else:
            curr.next = pList_right
            pList_right = pList_right.next
        curr = curr.next
    if pList_left == None:
        curr.next = pList_right
    if pList_right == None:
        curr.next = pList_left
    return merged_list.next

           

def divide_list(pList):
    if pList == None or pList.next == None:
        pList_left = pList
        pList_right = None
        return pList_left, pList_right
    else:
        mid_ptr = pList
        front_runner_ptr = pList.next
        while front_runner_ptr != None:
            front_runner_ptr = front_runner_ptr.next
            if front_runner_ptr != None:
                front_runner_ptr = front_runner_ptr.next
                mid_ptr = mid_ptr.next
        pList_left = pList
        pList_right = mid_ptr.next        
        mid_ptr.next = None
        return pList_left, pList_right        
                
            
# Complete the function below.

#For your reference:
#LinkedListNode {
#    int val
#    LinkedListNode next
#}

#def  mergeSortList(pList):



#f = open(os.environ['OUTPUT_PATH'], 'w')
    

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

res = mergeSortList(_pList);
#while (res != None):
#    f.write(str(res.val) + "\n")
#    res = res.next;
#f.close()
while(res != None):
    print(str(res.val))
    res = res.next

