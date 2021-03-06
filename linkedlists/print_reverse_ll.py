from linked_list_prototype import ListNode
from collections import deque

# @include
def print_linked_list_in_reverse(head):
    nodes = []
    while head:
        nodes.append(head.data)
        head = head.next
    while nodes:
        print(nodes.pop())
# @exclude

def print_linked_list(head):
    nodes = deque()
    while head:
        nodes.append(head.data)
        head = head.next

    while nodes:
        print(nodes.popleft())

def main():
    print_linked_list_in_reverse(ListNode(1, ListNode(2, ListNode(3, None))))
    print_linked_list(ListNode(1, ListNode(2, ListNode(3, None))))


if __name__ == '__main__':
    main()
