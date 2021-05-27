'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

https://leetcode.com/problems/add-two-numbers/
'''


# Definition for singly-linked list.
from typing import Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def get_next(l: ListNode) -> Tuple:
            if (l is None): 
                return (0, None)
            else: 
                return (l.val, l.next)

        def loop(l1: ListNode, l2: ListNode, carry: int) -> ListNode:
            if l1 == None and l2 == None and carry == 0:
                return None
            
            (x1, next1) = get_next(l1)
            (x2, next2) = get_next(l2)
            
            sum = x1 + x2 + carry
            x = sum % 10
            carry = sum // 10

            l1 = next1
            l2 = next2

            return ListNode(x, loop(next1, next2, carry))


        return loop(l1, l2, 0)