#!/bin/python3
import math
import sys
import os

class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def add(self, data):
        new_node = ListNode(data, self.head)
        self.head = new_node
        self.size +=1
    def print_list(self):
        this_node = self.head
        i = 0
        while this_node:
            print(i, '---' , this_node.data)
            this_node = this_node.next
            i +=1
    def reverse_print_list(self):
        prev = None
        current = self.head
        print('current before while ', current.data)
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def reverse_sub_array(self, s, f):
        dummy_head = sublist_head = ListNode(0,self)
        for _ in range(1,s):
            sublist_head = sublist_head.next
        sublist_iter = sublist_head.next
        for _ in range(f-s):
            temp = sublist_iter.next
            sublist_iter.next, temp.next, sublist_head.next = (temp.next, sublist_head.next, temp)
        return dummy_head.next
        #print('p---',prev.data)
        
            
a = LinkedList()
a.add(2)
a.add(4)
a.add(5)
a.add(6)
a.add(10)
a.print_list()
#a.reverse_print_list()
#a.print_list()
a.reverse_sub_array(2,4)
a.print_list()
