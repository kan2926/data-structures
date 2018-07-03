from collections import namedtuple

class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right  = None

def lca(tree, node0, node1):
    Status = namedtuple('Status', ('num_target_nodes', 'ancestor'))
    def lca_helper(tree, node0, node1):
        if tree is None:
            return Status(0, None)

        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes == 2:
            return left_result
        
        right_result = lca_helper(tree.right, node0, node1)
        if right_result.num_target_nodes ==2:
            return right_result

        num_target_nodes  = (left_result.num_target_nodes + right_result.num_target_nodes +
                                            (node0, node1).count(tree.data) )

        return Status(num_target_nodes, tree if num_target_nodes == 2 else None)

    return lca_helper(tree, node0, node1).ancestor

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
lca_node = lca(root, 4, 6)

print(lca_node.data)



