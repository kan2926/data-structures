class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right  = None

def sortedArrayToBST(arr, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    node = Node(arr[mid])

    node.left = sortedArrayToBST(arr, start, mid-1)
    node.right = sortedArrayToBST(arr, mid+1, end)
    return node

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


l = [1,2,3,4,5,6,7]
root= sortedArrayToBST(l, 0, len(l)-1)
print("In order --->")
inorder(root)
print("Pre order --->")
preorder(root)
