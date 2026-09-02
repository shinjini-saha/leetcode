from leetcode.depth_first_search.longest_valid_parentheses import longest_valid_parentheses


def test_longest_valid_parentheses():
    s = "(()"
    assert longest_valid_parentheses(s) == 2

    s = ")()())"
    assert longest_valid_parentheses(s) == 4

    s = ")(()))"
    assert longest_valid_parentheses(s) == 4

    s = "(()()"
    assert longest_valid_parentheses(s) == 4

    s = "((((()()"
    assert longest_valid_parentheses(s) == 4

    s = "()()))))"
    assert longest_valid_parentheses(s) == 4

    s = "()(())"
    assert longest_valid_parentheses(s) == 6
