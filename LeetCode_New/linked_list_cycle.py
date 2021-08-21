"""
https://leetcode.com/problems/linked-list-cycle/

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# put each node in a set, if .next in set, return true (Set is faster than dictionary)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        last = head
        track_map = set()

        while last:
            track_map.add(last)
            last = last.next
            if last in track_map:
                return True

        return False
