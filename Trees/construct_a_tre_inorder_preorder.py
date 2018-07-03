
class Node:
    def __init__(self, key):
        self.data = key
        self.right = None
        self.left = None
    
def buildTree(inOrder, preOrder, start, end):
    if start > end:
        return None

    root = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1

    if start == end:
        return root

    inIndex = search(inOrder, start, end, root.data)
    root.left = buildTree(inOrder, preOrder, start, inIndex-1)
    root.right = buildTree(inOrder, preOrder, inIndex+1, end)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def search(arr, start, end, value):
    for i in range(start, end+1):
        if arr[i] == value:
            return i


inOrder = ['D', 'B' ,'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']

buildTree.preIndex = 0
root = buildTree(inOrder, preOrder, 0, len(inOrder)-1)
print('inorder ----')
inorder(root)
print('preorder ----')
preorder(root)
