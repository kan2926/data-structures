
import sys
import os

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


def  isBST(root):
    if root is None:
        return 
    print(root.val)
    node = root
    while node is not None:
        
        

_size = int(input());


_str = input()
root = createTree(_str);
res = isBST(root);
print(str(int(res)) + "\n")

