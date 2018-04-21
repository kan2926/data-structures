
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def add(self,item):
        self.items.append(item)
    def front(self):
        return self.items[0]
    def pop(self):
        return self.items.pop(0)
    def printQ(self):
        for i in self.items:
            print(i , end = " ")
        print(" ")

def reverseQ(q):
    if q.isEmpty():
        return
    data  = q.front()
    q.pop()
    reverseQ(q)
    q.add(data)



q = Queue()
q.add(12)
q.add(89)
q.add(56)
q.add(45)
q.add(43)
reverseQ(q)
q.printQ()
