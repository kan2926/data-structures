class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right  = None

def printLevelOrder(root):
    if root is None:
        return
    q = []
    q.append(root)
    while len(q)> 0:
        print(q[0].data)
        temp = q.pop(0)
        if temp.left is not None:
            q.append(temp.left)
        if temp.right is not None:
            q.append(temp.right)

def flip_tree(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return root
    flippedroot = flip_tree(root.left)
    root.left.left = root.right
    root.left.right = root
    root.left = root.right = None
    return flippedroot

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print ("Level order traversal of given tree")
printLevelOrder(root)
flipped_root = flip_tree(root)
printLevelOrder(flipped_root)
