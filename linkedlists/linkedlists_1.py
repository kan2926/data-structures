class Node(object):
    def __init__(self, d, n= None):
        self.data = d
        self.next_node = n
    def get_next(self):
        return self.next_node
    def set_next(self,n):
        self.next_node = n
    def get_data(self):
        return self.data
    def set_data(self,d):
        self.data = d

class LinkedList(object):
    def __init__(self,r =None):
        self.root = r
        self.size = 0
        
    def get_size(self):
        return self.size
    
    def add(self,d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size +=1
        
    def remove(self,d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -=1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False
    
    def find (self,d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

    def print_list(self):
        this_node = self.root
        i = 0
        while this_node:
            print(i, '---' , this_node.get_data())
            this_node = this_node.get_next()
            i +=1
    def add_node(self,n):
        n.set_next(self.root)
        self.root = n
        self.size +=1       
    
    def sort_list(self):
        if(self.size > 1):
            this_node = self.root
            new_list = []
            while this_node:
                new_list.append(this_node.get_data())
                this_node = this_node.get_next()
            print(sorted(new_list, reverse=True))
            sortedList = LinkedList()
            for node in sorted(new_list, reverse=True):
                new_node = Node(node, self.root)
                sortedList.add_node(new_node)
            return sortedList
        return self
        
a = LinkedList()
a.add(4)
a.add(2)
a.add(9)

a.remove(2)
a.add(45)
a.add(23)
a.add(78)
print(a.get_size())
print(a.find(3))
print(a.find(2))
print(a.find(23))
a.print_list()
sorted_list = a.sort_list()
sorted_list.print_list()
