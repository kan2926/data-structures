class Node:
    def __init__(self, key):
        self.data = key
        self.left= None
        self.right = None

INT_MIN = -4294967296
INT_MAX = 4294967296
def isBst(root):
    if root is None:
        return True
    
    return isBstUtil(root, INT_MIN, INT_MAX)

def isBstUtil(node, mini, maxi):
    if node is None:
        return True

    if node.data < mini or node.data > maxi :
        return False

    return (isBstUtil(node.left, mini, node.data) and
             isBstUtil(node.right, node.data, maxi))

def is_binary_search_tree(root):

    def is_bst(node, min, max):
        if node.data <= min:
            return False

        if node.data >= max:
            return False

        left_ok = True
        right_ok = True

        if node.left is not None:
            left_ok = is_bst(node.left, min, node.data)
        if node.right is not None:
            right_ok = is_bst(node.right, node.data, max)

        return left_ok and right_ok

    if root is None:
        return True

    return is_bst(root, float('-inf'), float('inf'))

root= Node(4)
root.left = Node(2)
root.right  = Node(5)
root.left.left  = Node(1)
root.left.right  = Node(3)
root.left.left.right = Node(18)

print(isBst(root))
print(is_binary_search_tree(root))
