class Node:
    def __init__(self, key):
        self.data  = key
        self.left = None
        self.right = None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def is_mirror(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    return ( root1.data == root2.data and is_mirror(root1.left, root2.right)
              and is_mirror(root1.right, root2.left))


def is_symmetric(root):
    if root is None:
        return 
    return is_mirror(root.left, root.right)

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(2)
root.right.left = Node(4)
root.right.right = Node(3)

inorder(root)
print(is_symmetric(root))
