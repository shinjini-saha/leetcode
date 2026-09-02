from __future__ import annotations

import math

count_ref = {"current": 0}


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: ListNode | None = None):
        self.val = val
        self.next = next
        self.id = count_ref["current"]
        count_ref["current"] += 1

    def __str__(self):
        a = list_node_to_array(self)
        return a.__str__()

    def to_array(self):
        return list_node_to_array(self)

    @classmethod
    def from_array(cls, a: list[int]) -> ListNode | None:
        return create_list_node(a)


def create_list_node(a: list[int]) -> ListNode | None:
    head = None
    prev_node = None
    for item in a:
        node = ListNode(item)
        if head is None:
            head = node
        if prev_node is not None:
            prev_node.next = node
        prev_node = node
    return head


def list_node_to_array(head: ListNode | None) -> list[int]:
    seen = set()
    arr = []
    node = head
    while True:
        if node is None:
            break
        if node.id in seen:
            arr.append(math.inf)
            break
        arr.append(node.val)
        seen.add(node.id)
        node = node.next

    return arr
