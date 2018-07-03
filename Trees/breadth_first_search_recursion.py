class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def getHeight(node):
    if node is None:
        return 0
    else:
        lheight = getHeight(node.left)
        rheight = getHeight(node.right)

    if lheight > rheight:
        return lheight+1
    else:
        return rheight+1

def printGivenLevel(root, level):
    if root is None:
        return None
    if level == 1:
        print("%d"%(root.data))
    elif level > 1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)

def printLevelOrder(root):
    if root is None:
        return None
    h = getHeight(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print('Level order traversal --- ')
printLevelOrder(root)
