from leetcode.binary_search.median_of_two_sorted_arrays import find_median_sorted_arrays


def test_find_median():
    l1 = []
    l2 = [1]
    assert find_median_sorted_arrays(l1, l2) == 1

    l1 = [1]
    l2 = [1]
    assert find_median_sorted_arrays(l1, l2) == 1

    l1 = [1, 2]
    l2 = [3, 4]
    assert find_median_sorted_arrays(l1, l2) == 2.5

    l1 = [3, 4]
    l2 = [1, 2]
    assert find_median_sorted_arrays(l1, l2) == 2.5

    l1 = [2, 3, 4, 5, 6, 7]
    l2 = [1]
    assert find_median_sorted_arrays(l1, l2) == 4

    l1 = [1, 4, 6, 8, 19, 39, 1233]
    l2 = [4, 7, 9, 23, 65, 899]
    assert find_median_sorted_arrays(l1, l2) == 9

    l1 = [1, 2, 3, 4, 5]
    l2 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    assert find_median_sorted_arrays(l1, l2) == 9

    l1 = [2]
    l2 = [1, 3, 4]
    assert find_median_sorted_arrays(l1, l2) == 2.5

    l1 = [2, 2, 4, 4]
    l2 = [2, 2, 2, 4, 4]
    assert find_median_sorted_arrays(l1, l2) == 2

    l1 = [1, 4, 6, 8, 19, 39, 45]
    l2 = [4, 7, 9, 23, 65, 899]

    assert find_median_sorted_arrays(l1, l2) == 9
