class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None

def _insert_node_into_singlylinkedlist(head, tail, val):
    if head == None:
        head = LinkedListNode(val)
        tail = head
    else:
        node = LinkedListNode(val)
        tail.next = node
        tail = tail.next
    return tail

def find_intersection(L1, L2):
    def length(L):
        length = 0
        while L is not None:
            length += 1
            L = L.next
        return length

    L1_len, L2_len = length(L1), length(L2)
    if L1_len > L2_len:
        L1, L2 = L2, L1  # L2 is the longer list
    # Advances the longer list to get equal length lists.
    
    for _ in range(abs(L1_len - L2_len)):
        L2 = L2.next
    while L1 and L2:
        print('1 --- ',L1.val)
        print('2 ---', L2.val)
        if L1.val == L2.val:
            print('matched')
            return L1.val
        L1, L2 = L1.next, L2.next
    return -1  # None implies there is no overlap between L1 and L2.



if __name__ == "__main__":
    
    l1 = None
    l1_tail = None
    l1_size = int(input('L1 Size:'))
    l1_i = 0
    while l1_i < l1_size:
        l1_item = int(input())

        l1_tail = _insert_node_into_singlylinkedlist(l1, l1_tail, l1_item)
        if l1_i == 0:
            l1 = l1_tail
        l1_i += 1

    l2 = None
    l2_tail = None
    l2_size = int(input('L2 size:'))
    l2_i = 0
    while l2_i < l2_size:
        l2_item = int(input())

        l2_tail = _insert_node_into_singlylinkedlist(l2, l2_tail, l2_item)
        if l2_i == 0:
            l2 = l2_tail
        l2_i += 1

    #--------
    merge_at = int(input())
    l1_temp = l1
    i = 0
    while i < merge_at:
        l1_temp = l1_temp.next
        i += 1
    if l2_tail == None:
        l2 = l1_temp
    else:
        l2_tail.next = l1_temp
    #--------
        
    res = find_intersection(l1, l2);
    print(res)
##    while res != None:
##        print(str(res.val)+"\n")
##        res = res.next
