class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLL:
    def __init__(self):
        self.head = None

    def add_node(self, d):
        new_node = Node(d, self.head)
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def print_list(self):
        this_node = self.head
        if self.head == None:
            print('No elements in the DLL')
        while this_node:
            print(this_node.data)
            this_node = this_node.next
        return self

    def print_list_reverse(self):
        this_node = self.head
        prev_node = self.head
        while this_node:
            prev_node = this_node
            this_node = this_node.next
        #this_node points to last node
        while prev_node:
            print(prev_node.data)
            prev_node = prev_node.prev
        return self

    def remove_node(self,d):
        prev_node = self.head
        this_node = self.head
        if this_node.data == d:
            if this_node.next:
                self.head = this_node.next
                this_node.next.prev = None
            else:
                self.head = None
                return
        else:
            while this_node.next:
                if this_node.data == d:
                    prev_node.next = this_node.next
                    this_node.next = prev_node.prev
                    return True
                else:
                    prev_node = this_node
                    this_node = this_node.next
        return False

a = DoublyLL()
a.add_node(2)
a.add_node(4)
a.add_node(1)
a.add_node(6)
a.add_node(8)
a.add_node(12)
a.add_node(15)

print('print in original order')
a.print_list()
print('print in reverse order')
a.print_list_reverse()
a.remove_node(1)
print('after a node is removed')
a.print_list()
a.remove_node(8)
a.remove_node(6)
a.remove_node(4)
a.remove_node(2)
a.remove_node(12)
a.remove_node(15)
print('after 1 more node removed')
a.print_list()
a.remove_node(2)
print('removing node')
a.print_list()

