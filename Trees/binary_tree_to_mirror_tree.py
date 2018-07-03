class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right  = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def mirror_tree(root):
    if root is None:
        return 
    mirror_tree(root.left)
    mirror_tree(root.right)
    tmp = root.left
    root.left = root.right
    root.right = tmp

    return root
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
inorder(root)
root = mirror_tree(root)
print('mirror tree  --- ')
inorder(root)
