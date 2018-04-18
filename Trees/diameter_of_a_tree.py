

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    return 1+max(height(node.left), height(node.right))

def diameter(root):
    if root is None:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)
    
    return max(lheight+rheight+1, max(ldiameter, rdiameter))
    

def print_tree(root):
    if root is None:
        return
    print_tree(root.left)
    print(root.data)
    print_tree(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print_tree(root)
print(height(root))

print('diameter of the tree --- > ' , diameter(root))
