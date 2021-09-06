"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root) -> int:
        return self._maxDepth(root)

    def _maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_height = self._maxDepth(root.left)
            right_height = self._maxDepth(root.right)

        return max(left_height, right_height) + 1
