from algorithms.quicksort import quicksort


def test_quicksort():
    a = [6, 67, 21, 4, 6, 8, 20, 6, 9]

    quicksort(a)

    assert a == [4, 6, 6, 6, 8, 9, 20, 21, 67]
