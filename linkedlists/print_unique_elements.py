from linked_list_prototype import ListNode

def reverse_print_list(self):
        prev = None
        current = self
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self = prev
        return self

def print_list(head):
    while head != None:
        print(head.data)
        head = head.next

def get_unique_elements(head):
    hash_map = dict()
    curr = head
    if curr is None:
        return
    i = 1
    while curr != None:
        if curr.data in hash_map.keys():
            #increase count
            cnt = hash_map[curr.data]
            cnt += 1
            hash_map[curr.data] = cnt
        else:
            hash_map[curr.data] = i
        curr = curr.next

    curr = head
    count_unique_ele = 0
    unique_ele = []
    while curr != None:
        if hash_map[curr.data] == 1:
            count_unique_ele += 1
            unique_ele.append(curr.data)
        curr = curr.next

    if count_unique_ele == 0:
        print(' No unique elements in the list ')
    else:
        print(' unique elements : ', unique_ele)
        

L7 = ListNode(7,None)
L6 = ListNode(6,L7)
L5 = ListNode(2,L6)
L4 = ListNode(4,L5)
L3 = ListNode(4,L4)
L2 = ListNode(2,L3)
L1 =ListNode(1,L2)
#print_list(L1)
get_unique_elements(L1)
