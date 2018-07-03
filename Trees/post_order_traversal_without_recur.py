#!/bin/python

import sys

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTree(data):
    def deserialize():
        val = next(vals,None)
        if val == None:
            return None
        if val == '#':
            return None
        node = Node(int(val))
        node.left = deserialize()
        node.right = deserialize()
        return node
    vals = iter(data.split())

    return deserialize()

def printInorder(root):
    if root == None:
        return
    printInorder(root.left)
    print(root.val,)
    printInorder(root.right)


def  postorderTraversal(root):
    if root == None:
        return
    s = []
    node = root
    done = 0
    while not done:
        if node != None:
            s.append(node)
            node = node.left
        else:
            if len(s) > 0:
                node = s.pop()
                print(node.val)
                node = node.right
            else:
                done = 1
                

_size = int(input());


_str = input()
root = createTree(_str);
postorderTraversal(root);
