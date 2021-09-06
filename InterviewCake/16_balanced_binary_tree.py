"""
Write a function to see if a binary tree ↴ is "superbalanced".
A tree is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one.

https://www.interviewcake.com/question/python3/balanced-binary-tree?course=fc1&section=trees-graphs
"""
import unittest
# from icecream import ic as print


def is_balanced(root):
    depth = []
    if root is not None:

        _is_balanced(root, 0, depth)
        print('Depth - {}'.format(depth))
        if (len(depth) >= 2) or len(depth) == 2 and abs(depth[0] - depth[1]) > 1:
            print('Not superbalanced')
            return False
        else:
            print('Superbalanced')
            return True
    else:
        print('Superbalanced')
        return True

    # Determine if the tree is superbalanced

def _is_balanced(node, height, depth):
    if node is None:
        return height
    left_height = _is_balanced(node.left, height+1, depth)
    right_height = _is_balanced(node.right, height+1, depth)

    if left_height not in depth:
        depth.append(left_height)
    if right_height not in depth:
        depth.append(right_height)
    return max(left_height, right_height)

class Test(unittest.TestCase):

    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_full_tree(self):
        tree = Test.BinaryTreeNode(5)
        left = tree.insert_left(8)
        right = tree.insert_right(6)
        left.insert_left(1)
        left.insert_right(2)
        right.insert_left(3)
        right.insert_right(4)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_both_leaves_at_the_same_depth(self):
        tree = Test.BinaryTreeNode(3)
        left = tree.insert_left(4)
        right = tree.insert_right(2)
        left.insert_left(1)
        right.insert_right(9)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_one(self):
        tree = Test.BinaryTreeNode(6)
        left = tree.insert_left(1)
        right = tree.insert_right(0)
        right.insert_right(7)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_two(self):
        tree = Test.BinaryTreeNode(6)
        left = tree.insert_left(1)
        right = tree.insert_right(0)
        right_right = right.insert_right(7)
        right_right.insert_right(8)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_three_leaves_total(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right.insert_left(8)
        right.insert_right(5)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_both_subtrees_superbalanced(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right_left = right.insert_left(8)
        right.insert_right(5)
        right_left.insert_left(7)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_both_subtrees_superbalanced_two(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(2)
        right = tree.insert_right(4)
        left.insert_left(3)
        left_right = left.insert_right(7)
        left_right.insert_right(8)
        right_right = right.insert_right(5)
        right_right_right = right_right.insert_right(6)
        right_right_right.insert_right(9)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_three_leaves_at_different_levels(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(2)
        left_left = left.insert_left(3)
        left.insert_right(4)
        left_left.insert_left(5)
        left_left.insert_right(6)
        right = tree.insert_right(7)
        right_right = right.insert_right(8)
        right_right_right = right_right.insert_right(9)
        right_right_right.insert_right(10)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_only_one_node(self):
        tree = Test.BinaryTreeNode(1)
        result = is_balanced(tree)
        self.assertTrue(result)

    # def test_linked_list_tree(self):
    #     tree = Test.BinaryTreeNode(1)
    #     right = tree.insert_right(2)
    #     right_right = right.insert_right(3)
    #     right_right.insert_right(4)
    #     result = is_balanced(tree)
    #     self.assertTrue(result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
