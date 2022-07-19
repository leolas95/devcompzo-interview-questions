from typing import Optional


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l3 = ListNode()
    cur = l3

    while l1 and l2:
        if l1.val < l2.val:
            new_node = ListNode(l1.val)
            cur.next = new_node
            l1 = l1.next if l1 else None
            cur = cur.next
        else:
            new_node = ListNode(l2.val)
            cur.next = new_node
            cur = cur.next
            l2 = l2.next if l2 else None

    while l1:
        new_node = ListNode(l1.val)
        cur.next = new_node
        cur = cur.next
        l1 = l1.next if l1 else None

    while l2:
        new_node = ListNode(l2.val)
        cur.next = new_node
        cur = cur.next
        l2 = l2.next if l2 else None

    return l3.next


def print_list(node: ListNode):
    while node:
        if node.next:
            print(f'{node.val} -> ', end='')
        else:
            print(f'{node.val}')

        node = node.next


if __name__ == '__main__':
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(3)
    print_list(list1)

    list2 = ListNode(4)
    list2.next = ListNode(5)
    list2.next.next = ListNode(6)
    print_list(list2)

    result = merge_two_lists(list1, list2)
    print_list(result)




