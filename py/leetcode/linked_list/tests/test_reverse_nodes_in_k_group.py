from datastructures.linked_list import ListNode
from leetcode.linked_list.reverse_nodes_in_k_group import reverse_k_group, reverse_k_items


def test_reverse_k_group():

    node = ListNode.from_array([1, 2, 3, 4, 5, 6])
    assert str(reverse_k_group(node, 3)) == str([3, 2, 1, 6, 5, 4])

    node = ListNode.from_array([1, 2, 3, 4, 5])
    assert str(reverse_k_group(node, 3)) == str([3, 2, 1, 4, 5])


def test_reverse_k_items():
    node = ListNode.from_array([1, 2, 3, 4, 5])
    new1, new2 = reverse_k_items(node, 2)
    assert str(new1) == str([2, 1])
    assert str(new2) == str([3, 4, 5])
