"""
https://leetcode.com/problems/add-two-numbers/


"""
from InterviewCake.DataStructuresAlgorithms.linked_list import LinkedList
from icecream import ic as print

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def addTwoNumbers(l1, l2):

    head = None
    last = None
    carry = 0

    while l1 or l2:
        res_val = l1.val + l2.val + carry
        carry = 0
        if res_val >= 10:
            res_val = res_val % 10
            carry = 1

        if head is None:
            head = ListNode(res_val)
            last = head
        else:
            last.next = ListNode(res_val)
            last = last.next

        print(l1.val, l2.val, res_val)
        l1 = l1.next
        l2 = l2.next

    while l1.next:
        last.next = ListNode(l1.val+carry)
        last = last.next

    while l2.next:
        last.next = ListNode(l2.val+carry)
        last = last.next

    if carry == 1:
        last.next = ListNode(carry)
        last = last.next

    while head:
        print(head.val)
        head = head.next


# l1 = [2,4,3]
l1 = ListNode(2)
l1.next = ListNode(2)
l1.next.next = ListNode(9)

# l2 = [5,6,5]
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(5)
print(addTwoNumbers(l1, l2))
