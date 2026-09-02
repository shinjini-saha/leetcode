# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# Return a boolean indicating whether the matching covers the entire input string (not partial).

from typing import Dict, Tuple


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return is_match(s, p)


def is_match(s: str, p: str) -> bool:
    memo = {}

    return is_match_helper(s, p, 0, 0, memo)


def is_match_helper(s: str, p: str, s_i: int, p_i: int, memo: Dict[Tuple[int, int], bool]) -> bool:
    key = (s_i, p_i)
    if key in memo:
        return memo[key]

    if p_i >= len(p):
        res = s_i >= len(s)
        memo[key] = res
        return res
    # base case, we've reached the end of s
    if s_i >= len(s):
        # there are only two acceptable options
        res = pattern_matches_empty_str(p, p_i)
        memo[key] = res
        return res

    p_char = p[p_i]
    s_char = s[s_i]

    # check if the next char is '*'
    p_next_char = p[p_i + 1] if (p_i + 1 < len(p)) else None

    char_is_match = is_char_match(s_char, p_char)
    # if there are no more pattern characters, we have to match the s_char AND
    # have no more s chars left
    if p_next_char is None:
        res = char_is_match and (s_i == len(s) - 1)
        memo[key] = res
        return res
    # if it's not a '*', we have to match the s_char and then try is_match again
    if p_next_char != "*":
        res = char_is_match and is_match_helper(s, p, s_i + 1, p_i + 1, memo)
        memo[key] = res
        return res

    # now it is a '*'. We have some cases
    if char_is_match:
        res = (
            # use up p_char + '*' only
            is_match_helper(s, p, s_i, p_i + 2, memo)
            or
            # use up s_char AND p_char + '*'
            is_match_helper(s, p, s_i + 1, p_i + 2, memo)
            or
            # use up s_char only
            is_match_helper(s, p, s_i + 1, p_i, memo)
        )
        memo[key] = res
        return res

    # if it's not a match, the only option is to use up p_char + '*' only
    res = is_match_helper(s, p, s_i, p_i + 2, memo)
    memo[key] = res
    return res


def is_char_match(s_char: str, p_char: str):
    return p_char == "." or p_char == s_char


def pattern_matches_empty_str(p: str, p_i: int):
    remaining_length = len(p) - p_i
    if remaining_length == 0:
        return True

    if remaining_length % 2 != 0:
        return False

    for i in range(p_i, len(p), 2):
        if p[i + 1] != "*":
            return False

    return True
