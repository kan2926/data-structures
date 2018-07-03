class Node:
    def __init__(self, key):
        self.val = key
        self.left= None
        self.right = None

INT_MIN = -4294967296
INT_MAX = 4294967296

def largestbst(root):
    if root is None:
        return 0

    max_size = [1]
    def largestBSTsubtreehelper(root):
        if root.left is None and root.right is None:
            return 1, root.val, root.val

        left_size, left_min, left_max = 0, root.val, root.val
        if root.left is not None:
            left_size, left_min, left_max = largestBSTsubtreehelper(root.left)

        right_size, right_min, right_max = 0, root.val, root.val
        if root.right is not None:
            right_size, right_min, right_max = largestBSTsubtreehelper(root.right)

        size = 0
        if (( root.left is None or left_size > 0 ) and
           ( root.right is None or right_size > 0) and
          left_max <=root.val <= right_max ):
               size = 1 + left_size + right_size
               max_size[0] = max(max_size[0],size)
        return size, left_min, right_max

    largestBSTsubtreehelper(root)
    return max_size[0]
    
    

root = Node(25)
root.left = Node(18)
root.left.left = Node(19)
root.left.left.right = Node(15)
root.left.right = Node(20)
root.left.right.left = Node(18)
root.left.right.right = Node(25)
root.right = Node(50)
root.right.left = Node(35)
root.right.left.left = Node(20)
root.right.left.left.right = Node(25)
root.right.left.right = Node(40)
root.right.right = Node(60)
root.right.right.left = Node(55)
root.right.right.right = Node(70)
print(largestbst(root))
