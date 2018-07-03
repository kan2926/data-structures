class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def inorder(root,res):
    if root:
        inorder(root.left,res)
        res.append(root.val)
        inorder(root.right,res)
        return res
def search(root, key):
    if root is None or root.val == key:
        return True if root else False
    if root.val < key:
        return True if search(root.right, key) else False
    return True if search(root.left, key) else False

def minValueNode(node):
    current = node
    while current is not None:
        current = current.left
    return current

def delete(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

def mergesort(l1,l2):
    m = len(l1)
    n = len(l2)
    i = 0
    j = 0
    l3=[]
    while i < m and j < n :
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i += 1
        else:
            l3.append(l2[j])
            j += 1
    l3 += l1[i:]
    l3 += l2[j:]
    return l3
        

r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))
l1 = inorder(r,[])
print(l1)

p = Node(3)
insert(p, Node(22))
insert(p,Node(42))
insert(p,Node(10))
insert(p,Node(12))
insert(p,Node(14))
l2 = inorder(p,[])
print(l2)
l3 = mergesort(l1,l2)
print(l3)
