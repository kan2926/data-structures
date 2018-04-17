class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)

def implement_queue(operations):
    s = []
    res = []
    if operations is None:
        return None
    
    while operations:
        if operations.data > 0:
            s.append(operations.data)
        else:
            if s:
                res.append(s[-1])
                s.pop()
            else:
                res.append(-1)
        print(res)
        operations = operations.next
    return res


if __name__ == '__main__':

    operations_count = int(input())

    operations = SinglyLinkedList()

    for _ in range(operations_count):
        operations_item = int(input())
        operations.insert_node(operations_item)
    res = implement_queue(operations.head)

    #print_singly_linked_list(res, '\n')
    print(res)
