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

def find_max_depth(root):
    if root is None:
        return None
    
    if root.left is None and root.right is None:
        return 1
    if root.left is  None:
        return find_max_depth(root.right)+1
    if root.right is None:
        return find_max_depth(root.left)+1

    return max(find_max_depth(root.left), find_max_depth(root.right))+1


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right  = Node(5)
root.left.right.left = Node(6)
root.right = Node(3)
inorder(root)
print('min depth --- ' ,find_max_depth(root))
