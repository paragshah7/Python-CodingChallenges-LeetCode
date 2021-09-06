"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        return self._invertTree(root)

    def _invertTree(self, root):
        if root is None:
            return
        else:
            # Take left and right subtree
            left = self._invertTree(root.left)
            right = self._invertTree(root.right)

            # Now give this right subtree to left node and left subtree to right node
            root.left = right
            root.right = left

        return root