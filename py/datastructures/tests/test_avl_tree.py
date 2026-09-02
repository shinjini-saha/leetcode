from datastructures.avl_tree import AVLTree


def test_avl_tree():

    tree = AVLTree()
    tree.insert(4)
    tree.insert(3)

    assert str(tree) == (
        """
4
    3"""
    )

    tree.insert(5)

    assert str(tree) == (
        """
    5
4
    3"""
    )

    tree.insert(2)

    assert str(tree) == (
        """
    5
4
    3
        2"""
    )

    tree.insert(2.5)
    tree.insert(1)

    assert str(tree) == (
        """
        5
    4
3
        2.5
    2
        1"""
    )

    tree.insert(6)

    assert str(tree) == (
        """
        6
    5
        4
3
        2.5
    2
        1"""
    )

    tree.insert(7)

    assert str(tree) == (
        """
            7
        6
    5
        4
3
        2.5
    2
        1"""
    )

    tree.insert(8)

    assert str(tree) == (
        """
            8
        7
            6
    5
        4
3
        2.5
    2
        1"""
    )

    tree.insert(9)

    assert str(tree) == (
        """
            9
        8
    7
            6
        5
            4
3
        2.5
    2
        1"""
    )

    tree.insert(10)

    assert str(tree) == (
        """
            10
        9
            8
    7
            6
        5
            4
3
        2.5
    2
        1"""
    )

    tree.insert(11)

    assert str(tree) == (
        """
            11
        10
    9
        8
7
            6
        5
            4
    3
            2.5
        2
            1"""
    )

    tree.insert(12)

    assert str(tree) == (
        """
            12
        11
            10
    9
        8
7
            6
        5
            4
    3
            2.5
        2
            1"""
    )
