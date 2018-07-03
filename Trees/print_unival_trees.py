
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



def  findSingleValueTrees(node):
    if node is None:
        return None
    path = ['' for i in range(100)]
    pathlen = 0
    printunivalTree(node, path, pathlen)

def printunivalTree(node, path, pathlen):
    if node is None:
        return None
    path[pathlen] = node.val
    pathlen += 1
    if node.left is None and node.right is None:
        printTree(path, pathlen)
    else:
        printunivalTree(node.left, path, pathlen)
        printunivalTree(node.right, path, pathlen)
   
def printTree(path, pathlen):
    for i in range(pathlen):
        if path[i] in path:
            if path[i] == path[i+1]:
                print(path[i], end = ' ')
            elif path[i] == path[i-1]:
                print('else ',path[i], end = ' ')
            else:
                print('no')


_size = int(input());


_str = input()
root = createTree(_str);
res = findSingleValueTrees(root);
print(str(res) + "\n")

