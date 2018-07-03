class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def InOrder_without_recur(root):
    if root is None:
        return
    q = []
    done = 0
    current = root
    while not done:
        if current is not None:
            q.append(current)
            current = current.left

        else:
            if len(q) > 0:
                current = q.pop()
                print(current.data)
                current = current.right
            else:
                done = 1
        


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right  = Node(5)
InOrder_without_recur(root)
