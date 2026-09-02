# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes
# is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.
from __future__ import annotations

from datastructures.linked_list import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        return reverse_k_group(head, k)


def reverse_k_group(head: ListNode | None, k: int) -> ListNode | None:
    if head is None:
        return head
    if k <= 1:
        return head

    first_reversed_head = None
    node = head
    prev_final = None
    while True:
        reverse_head, next_head = reverse_k_items(node, k)
        if prev_final is not None:
            prev_final.next = reverse_head
        prev_final = node

        if first_reversed_head is None:
            first_reversed_head = reverse_head
        if next_head is None:
            return first_reversed_head
        node = next_head


def reverse_k_items(head: ListNode | None, k) -> tuple[ListNode | None, ListNode | None]:
    if head is None:
        return None, None
    count = 0
    prev_node: ListNode | None = None
    curr_node = head
    while True:
        next_node = curr_node.next
        curr_node.next = prev_node
        count += 1
        if count == k:
            return curr_node, next_node
        if next_node is None:
            # we've reached the end of the road without having reached k items, undo the work
            res1, _ = reverse_k_items(curr_node, count)
            return res1, None

        curr_node, prev_node = next_node, curr_node
