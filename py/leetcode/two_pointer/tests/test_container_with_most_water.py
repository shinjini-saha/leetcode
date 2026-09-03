from leetcode.two_pointer.container_with_most_water import max_area


def test_max_area():

    height = [1, 1]
    assert max_area(height) == 1

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert max_area(height) == 49
