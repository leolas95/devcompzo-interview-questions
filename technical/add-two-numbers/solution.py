from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        # Init result list
        l3 = ListNode()
        base = l3

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            res = carry + v1 + v2

            if res > 9:
                val = res % 10
                carry = res // 10
            else:
                val = res
                carry = 0

            l3.next = ListNode(val)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            l3 = l3.next

        return base.next

#         while (l1 is not None) or (l2 is not None):
#             res = carry + l1.val + l2.val
#             if res > 9:
#                 last_digit = res % 10
#                 carry = res // 10
#                 newNode = ListNode(last_digit)
#             else:
#                 newNode = ListNode(res)
#                 carry = 0

#             if l3.val == -1:
#                 l3 = newNode
#             else:
#                 l3.next = newNode

#             l1 = l1.next
#             l2 = l2.next
#             l3 = l3.next

#         while l1 is not None:
#             res = carry + l1.val
#             if res > 9:
#                 last_digit = res % 10
#                 carry = res // 10
#                 newNode = ListNode(last_digit)
#             else:
#                 newNode = ListNode(res)
#                 carry = 0

#             l1 = l1.next
#             l3 = l3.next

#         while l2 is not None:
#             res = carry + l2.val
#             if res > 9:
#                 last_digit = res % 10
#                 carry = res // 10
#                 newNode = ListNode(last_digit)
#             else:
#                 newNode = ListNode(res)
#                 carry = 0

#             l2 = l2.next
#             l3 = l3.next

#         if carry > 0:
#             newNode = ListNode(carry)
#             l3.next = newNode
#             l3 = l3.next


