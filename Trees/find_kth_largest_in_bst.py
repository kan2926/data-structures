class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def inorder(root,res):
    if root:
        inorder(root.left,res)
        res.append(root.val)
        inorder(root.right,res)
        return res
def search(root, key):
    if root is None or root.val == key:
        return True if root else False
    if root.val < key:
        return True if search(root.right, key) else False
    return True if search(root.left, key) else False

def find_k_largest_in_bst(tree, k):
    def find_k_largest_in_bst_helper(tree):
        if tree and len(k_largest_elements) < k:
            find_k_largest_in_bst_helper(tree.right)
            if len(k_largest_elements) <k:
                k_largest_elements.append(tree.val)
                find_k_largest_in_bst_helper(tree.left)

    k_largest_elements = []
    find_k_largest_in_bst_helper(tree)
    return k_largest_elements
    

r = Node(19)
insert(r, Node(7))
insert(r, Node(3))
insert(r, Node(2))
insert(r, Node(5))
insert(r, Node(11))
insert(r, Node(17))
insert(r, Node(13))
insert(r, Node(43))
insert(r, Node(23))
insert(r, Node(47))
insert(r, Node(37))
insert(r, Node(29))
insert(r, Node(31))
insert(r, Node(41))
insert(r, Node(53))

l1 = inorder(r, [])
print(l1)
k = int(input('Enter input k:'))
print(find_k_largest_in_bst(r,k))








