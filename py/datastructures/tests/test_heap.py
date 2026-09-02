from datastructures.heap import MinHeap


def test_min_heap():
    m = MinHeap()

    m.insert(4)
    assert str(m) == str([4])

    m.insert(24)
    assert str(m) == str([4, 24])

    m.insert(45)
    assert str(m) == str([4, 24, 45])

    m.insert(3)
    assert str(m) == str([3, 4, 45, 24])

    m.insert(2)
    assert str(m) == str([2, 3, 45, 24, 4])

    m.insert(34)
    assert str(m) == str([2, 3, 34, 24, 4, 45])

    m.insert(1)
    assert str(m) == str([1, 3, 2, 24, 4, 45, 34])

    assert m.pop() == 1
    assert m.pop() == 2
    assert m.pop() == 3
    assert m.pop() == 4
    assert m.pop() == 24
    assert m.pop() == 34
    assert m.pop() == 45
    assert m.pop() is None
