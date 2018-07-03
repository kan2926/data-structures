class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def sum_of_left_subtree(root):
    if root is None:
        return 0
    curr = root
    if curr.left is None and curr.right is None:
        return root.data
    left_sum = sum_of_left_subtree(root.left)
    right_sum = sum_of_left_subtree(root.right)
    root.data += left_sum

    return root.data + right_sum

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(6)
root.left.left = Node(4)
root.left.right = Node(5)
inorder(root)
sum_of_left_subtree(root)
print('sum---')
inorder(root)
