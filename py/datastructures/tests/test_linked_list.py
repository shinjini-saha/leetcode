from datastructures.linked_list import ListNode


def test_linked_list():
    node = ListNode.from_array([4, 6, 3, 7])

    assert str(node) == str([4, 6, 3, 7])

    assert node is not None
    assert str(node.next) == str([6, 3, 7])
