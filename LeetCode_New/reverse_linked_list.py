"""
Reverse a Linked List
"""

# from icecream import ic as print
import time


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


head = None
last = None

# create linked list
for i in range(1,6):
    if head is None:
        head = ListNode(i)
        last = head
    else:
        last.next = ListNode(i)
        last = last.next

# print linked list
# last = head
# while last:
#     print(last.val, end=' -> ')
#     last = last.next
# print('None')


def reverse_ll(head):
    first = None
    last = head
    print('Original linked list - ')
    while last:
        print(last.val, end=' -> ')

        # Reverse logic
        if first is None:
            first = ListNode(last.val)
        else:
            new_node = ListNode(last.val)
            new_node.next = first
            first = new_node

        last = last.next
    print('None')

    # print reverse ll
    print('\nReverse linked list - ')
    last = first
    while last:
        print(last.val, end=' -> ')
        last = last.next
    print('None')


reverse_ll(head)
