from leetcode.rolling_hash.shortest_palindrome import shortest_palindrome


def test_shortest_palindrome():
    s = "aacecaaa"
    assert shortest_palindrome(s) == "aaacecaaa"

    s = "abcd"
    assert shortest_palindrome(s) == "dcbabcd"
