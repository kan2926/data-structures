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

def are_mirror_trees(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return (root1.data == root2.data and
            are_mirror_trees(root1.left, root2.right) and
            are_mirror_trees(root1.right, root2.left))

root1 = Node(1)
root1.left = Node(3)
root1.right = Node(2)
root1.right.left = Node(5)
root1.right.right = Node(4)
print('root1---')
inorder(root1)

root2 = Node(1)
root2.left = Node(2)
root2.left.left = Node(4)
root2.left.right = Node(5)
root2.right = Node(3)
        
print('root2=--')
inorder(root2)

print(are_mirror_trees(root1, root2))
