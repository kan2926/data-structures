from collections import namedtuple

class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right  = None

def is_balanced_binary_tree(tree):
    BalancedStatusWithHeight = namedtuple('BalancedStatusWithHeight', ('balanced','height'))

    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1)

        left_result = check_balanced(tree.left)
        if not left_result:
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result:
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height)+1
        return BalancedStatusWithHeight(is_balanced, height)
    return check_balanced(tree).balanced                                                            

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)
root.right = Node(3)
root.right.left = Node(6)
print(is_balanced_binary_tree(root))
