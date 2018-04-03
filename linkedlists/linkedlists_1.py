class Node(object):

    def __init__ (self, d, n = None):
        self.data = d
        self.next_node = n

    def get_next (self):
        return self.next_node

    def set_next (self, n):
        self.next_node = n

    def get_data (self):
        return self.data

    def set_data (self, d):
        self.data = d

    def has_next(self):
        if self.get_next() is None:
           return False
        else:
          return True
    def to_string(self):
        return "Node Value: "+ str(self.data)
    


class LinkedList (object):

    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def get_size (self):
        return self.size

    def add_node (self, n):
        n.set_next(self.root);
        self.root = n;
        self.size += 1;

    def add (self, d):
        new_node = Node (d, self.root)
        self.root = new_node
        self.size += 1

    def remove (self, d):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True		
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False  # data not found

    def find (self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None
    def print_list(self):
        if self.root is None:
            return
        current = self.root
        print(current.to_string())
        while current.has_next():
            current = current.get_next();
            print(current.to_string())
        return self; 

    def sort (self):
        if self.size > 1:
                newlist = [];
                current = self.root;
                newlist.append(self.root);
                while current.has_next():
                        current = current.get_next();
                        newlist.append(current);
                newlist = sorted(newlist, key = lambda node: node.get_data(), reverse = True);
                newll = LinkedList();
                for node in newlist:
                        newll.add_node(node);
                return newll;
                   

aList = LinkedList()
aList.add(15)
aList.add(28)
aList.add(12)
print("size="+str(aList.get_size()))
aList.remove(8)
print("size="+str(aList.get_size()))
print(aList.remove(12))
print("size="+str(aList.get_size()))
print(aList.find(1))
aList.add(99)
aList.add(23)
aList.add(0)
aList.print_list()

bList=aList.sort()
print('sorted')
bList.print_list()

