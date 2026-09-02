from leetcode.dynamic_programming.regular_expression_matching import is_match, pattern_matches_empty_str


def test_is_match():

    assert is_match("aa", "a") is False
    assert is_match("aa", "a*") is True
    assert is_match("aa", "aa*") is True
    assert is_match("aa", ".*") is True
    assert is_match("aab", "c*a*b") is True
    assert is_match("aaaaaaaaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*") is False


def test_pattern_matches_empty_str():

    assert pattern_matches_empty_str("", 0) is True
    assert pattern_matches_empty_str("p", 0) is False
    assert pattern_matches_empty_str("p", 1) is True
    assert pattern_matches_empty_str("p*", 0) is True
    assert pattern_matches_empty_str("p*p*", 2) is True
    assert pattern_matches_empty_str("p*p*pp*", 2) is False
