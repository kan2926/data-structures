class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def printLevelOrderByLine(root):
    if root is None:
        return
    q = []
    q.append(root)
    while True:
        nodeCount = len(q)
        if nodeCount == 0:
            break

        while nodeCount > 0:
            k = q.pop(0)
            print(k.data, end = " ")
            if k.left is not None:
                q.append(k.left)
            if k.right is not None:
                q.append(k.right)
            nodeCount -= 1
        print()



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left = Node(4)
root.left.right = Node(5)
printLevelOrderByLine(root)
