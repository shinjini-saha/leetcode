from leetcode.depth_first_search.max_points import max_points


def test_max_points():

    edges = [[0, 1], [1, 2], [2, 3]]
    coins = [10, 10, 3, 3]
    k = 5
    assert max_points(edges, coins, k) == 11

    edges = [[0, 1], [0, 2]]
    coins = [8, 4, 4]
    k = 0
    assert max_points(edges, coins, k) == 16

    edges = [[1, 0], [0, 2], [1, 3]]
    coins = [9, 3, 8, 9]
    k = 0
    assert max_points(edges, coins, k) == 29

    edges = [[0, 1], [0, 2], [1, 3]]
    coins = [9, 3, 8, 9]
    k = 0
    assert max_points(edges, coins, k) == 29

    edges = [[0, 1], [0, 2], [3, 2], [0, 4]]
    coins = [5, 6, 8, 7, 4]
    k = 7
    assert max_points(edges, coins, k) == 8
