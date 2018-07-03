class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right  = None

def inorder(root):
    if root is None:
        return None
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def concatenate(alist, blist):
    if alist is None:
        return blist
    if blist is None:
        return alist
    leftlast = alist.left
    rightlast = blist.left

    leftlast.right = blist
    blist.left = leftlast
    alist.left = rightlast
    blist.right = alist
    return alist

def TreeToList(root):
    if root is None:
        return None
    left = TreeToList(root.left)
    right = TreeToList(root.right)
    root.left = root.right = root
    return concatenate(concatenate(left, root), right)
    
def displayCLL(head):
    curr = head
    while curr:
        print(curr.data, end=' ')
        curr = curr.right
        if curr == head:
            break
        
root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(5)
inorder(root)
head = TreeToList(root)
displayCLL(head)
