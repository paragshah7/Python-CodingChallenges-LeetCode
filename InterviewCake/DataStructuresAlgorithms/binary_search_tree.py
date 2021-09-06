"""
Implement binary search tree
https://www.youtube.com/watch?v=f5dU3xoE6ms&list=PLEJyjB1oGzx3iTZvOVedkT8nZ2cG105U7&index=5
"""
from queue import Queue
import time

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BST:
    """ root in bst, head in linked list """
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            cur_node = self.root
            self._insert(value, cur_node)

    # Use static method so that you can pass node as well which is not passed in original method
    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)

        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)

        # duplicate value
        else:
            print('Value already in tree')

    # Pre order traversal / DFS
    def print_tree(self):
        if self.root is None:
            print('Empty tree')
        self._print_tree(self.root)

    # Use static method so that you can pass node as well which is not passed in original method
    # https://www.programiz.com/dsa/binary-tree
    def _print_tree(self, cur_node):
        """
        cur_node
        print first - pre-order (dfs)
        print middle - in-order (sorted)
        print last - post-order
        """
        if cur_node is not None:
            print(cur_node.value)
            self._print_tree(cur_node.left)
            self._print_tree(cur_node.right)

    # Level order traversal / BFS
    def print_tree_bfs(self):
        if self.root is None:
            print('Empty tree')
        self._print_tree_bfs(self.root)

    def _print_tree_bfs(self, cur_node):
        q = Queue()
        tree = ''

        if cur_node is not None:
            print(cur_node.value)
            tree += str(cur_node.value) + '\n'
            q.enqueue(cur_node)

            while not q.is_empty():
                cur_node = q.dequeue()
                if cur_node.left:
                    print(cur_node.left.value)
                    tree += str(cur_node.left.value) + '_/  '
                    q.enqueue(cur_node.left)
                if cur_node.right:
                    print(cur_node.right.value)
                    q.enqueue(cur_node.right)
                    tree += '  \_' + str(cur_node.right.value) + '\n'

        print(tree)

    def height(self):
        return self._height(self.root)

    def _height(self, cur_node):
        if cur_node is None:
            return 0
        else:
            left_height = self._height(cur_node.left)
            right_height = self._height(cur_node.right)

        return max(left_height, right_height) + 1

    def search(self, value):
        if self.root is None:
            return False
        return self._search(value, self.root)

    def _search(self, value, cur_node):
        if cur_node.value == value:
            return True
        elif value < cur_node.value and cur_node.left is not None:
            return self._search(value, cur_node.left)
        elif value > cur_node.value and cur_node.right is not None:
            return self._search(value, cur_node.right)
        else:
            return False


bst = BST()
bst.insert(9)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(10)
# bst.print_tree()
print(bst.height())
# print(bst.search(100))
# bst.height()
