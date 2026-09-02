from datastructures.linked_list import ListNode
from leetcode.heap.merge_k_sorted_lists import merge_k_lists


def test_find_median():
    a = ListNode.from_array([1, 2, 4])
    b = ListNode.from_array([1, 3, 4])

    assert str(merge_k_lists([a, b])) == str([1, 1, 2, 3, 4, 4])

    a = ListNode.from_array([])
    b = ListNode.from_array([-2])
    c = ListNode.from_array([-3, -2, 1])
    assert str(merge_k_lists([a, b, c])) == str([-3, -2, -2, 1])
