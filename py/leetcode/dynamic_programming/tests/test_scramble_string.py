from leetcode.dynamic_programming.scramble_string import is_scramble


def test_scramble_string():

    s1 = "great"
    s2 = "great"

    assert is_scramble(s1, s2) is True

    s1 = "great"
    s2 = "rgeat"

    assert is_scramble(s1, s2) is True

    s1 = "aegrt"
    s2 = "rgeat"

    assert is_scramble(s1, s2) is True

    s1 = "abcde"
    s2 = "caebd"
    assert is_scramble(s1, s2) is False

    s1 = "abcdbdacbdac"
    s2 = "bdacabcdbdac"
    assert is_scramble(s1, s2) is True

    s1 = "grating"
    s2 = "grating"
    assert is_scramble(s1, s2) is True
