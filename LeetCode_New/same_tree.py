"""
https://leetcode.com/problems/same-tree/solution/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q) -> bool:
        return self._isSameTree(p, q)

    def _isSameTree(self, p, q):
        if p is None and q is None:
            return True

        # imp - if either tree is None or both values don't match
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        left = self._isSameTree(p.left, q.left)
        right = self._isSameTree(p.right, q.right)

        # imp
        return left and right