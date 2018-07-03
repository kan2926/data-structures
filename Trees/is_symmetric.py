
class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right  = None

def is_symmetric(root):

    def check_is_symmetric(sub_tree_0, sub_tree_1):
        if not sub_tree_0 and not sub_tree_1:
            return True
        elif sub_tree_0 and sub_tree_1:
            return (sub_tree_0.data == sub_tree_1.data
                    and check_is_symmetric(sub_tree_0.left, sub_tree_1.right)
                    and check_is_symmetric(sub_tree_0.right, sub_tree_1.left))
        return False
    return not root or check_is_symmetric(root.left, root.right)


root = Node(314)
root.left = Node(6)
root.left.right = Node(2)
root.left.right.right = Node(3)
root.right = Node(6)
root.right.left = Node(2)
root.right.left.left = Node(3)
# root.right.left.left.left = Node(7)   -- false
print(is_symmetric(root))
