"""
Implement linked list
https://www.youtube.com/watch?v=JlMyYuY1aXU&list=PLEJyjB1oGzx3iTZvOVedkT8nZ2cG105U7&index=3
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node

    def delete(self):
        if self.head is None:
            print('linked list empty')
            return

        cur_node = self.head
        prev_node = cur_node
        while cur_node.next:
            prev_node = cur_node
            cur_node = cur_node.next
        prev_node.next = None

    def print_linked_list(self):
        if self.head is None:
            print('linked list empty')
            return
        cur_node = self.head
        print('head -> ', end='')
        while cur_node.next:
            print(cur_node.value, '-->', end=' ')
            cur_node = cur_node.next
        print(cur_node.value, '-> None')

    def search(self, value):
        if self.head is None:
            print('linked list empty')
            return
        if self.head.value == value:
            return True

        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
            if cur_node.value == value:
                return True
        return False


ll = LinkedList()
ll.insert(1)
ll.insert(2)
print(ll.search(2))
ll.delete()
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.print_linked_list()
print(ll.search(6))
