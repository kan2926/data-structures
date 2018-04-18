
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
    print(root.val)
    printInorder(root.right)

def  printAllPaths(root):
    pathlen=0
    path = [ ' ' for i in range(1000)]
    printPathsRecur(root, path, pathlen)
    
def printPathsRecur(root, path, pathlen):
    if root is None :
        return
    path[pathlen] = root.val
    pathlen += 1
    if root.left is None and root.right is None:
        printTree(path, pathlen)
    else:
        printPathsRecur(root.left, path, pathlen)
        printPathsRecur(root.right, path, pathlen)
    
def printTree(path, pathlen):
    for i in range(pathlen):
        print(path[i], end = ' ')
    print()

        
_size = int(input());


_str = input()
root = createTree(_str);
printAllPaths(root);
#printInorder(root)
