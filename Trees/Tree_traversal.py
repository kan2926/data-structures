class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
def printPreorder(root):
    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val)

def printInorder(root):
    if root:
        printPostorder(root.left)
        print(root.val)        
        printPostorder(root.right)
        

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right= Node(5)

print('Pre order traversal --- ')
printPreorder(root)

print('Post order traversal --- ')
printPostorder(root)

print('In order traversal --- ')
printInorder(root)



