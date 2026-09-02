from __future__ import annotations

import heapq

from datastructures.linked_list import ListNode


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        return merge_k_lists(lists)


def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None:
    uniqueness_i = 0
    heap = []
    for i, node in enumerate(lists):
        uniqueness_i += 1
        if node is not None:
            heap.append((node.val, uniqueness_i, node))

    heapq.heapify(heap)

    res: ListNode | None = None
    res_curr_node: ListNode | None = None

    while len(heap) > 0:
        uniqueness_i += 1
        min_val, _, min_node = heapq.heappop(heap)
        if res_curr_node is None:
            res = ListNode(min_val)
            res_curr_node = res
        else:
            res_curr_node.next = ListNode(min_val)
            res_curr_node = res_curr_node.next

        if min_node.next is not None:
            heapq.heappush(heap, (min_node.next.val, uniqueness_i, min_node.next))
    return res


def print_node_list(lists: list[tuple[int, int, ListNode]]):
    print("<lists>")
    for i, (_, _, node) in enumerate(lists):
        print("    ", i, node)
    print("</lists>")
