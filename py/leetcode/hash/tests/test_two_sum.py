from leetcode.hash.two_sum import two_sum


def test_two_sums():
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([1, 5, 7, 9, 14, 63, 90], 16) == [2, 3]
