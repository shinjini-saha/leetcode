# We can scramble a string s to get a string t using the following algorithm:

# If the length of the string is 1, stop.
# If the length of the string is > 1, do the following:
# Split the string into two non-empty substrings at a random index, i.e., if the string is s,
# divide it to x and y where s = x + y.
# Randomly decide to swap the two substrings or to keep them in the same order. i.e., after
# this step, s may become s = x + y or s = y + x.
# Apply step 1 recursively on each of the two substrings x and y.
#
# Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of
# s1, otherwise, return false.


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return is_scramble(s1, s2)


def is_scramble(s1: str, s2: str, memo=None) -> bool:
    if memo is None:
        memo = {}
    key = f"{s1};{s2}"
    if key in memo:
        return memo[key]
    if len(s1) != len(s2):
        return False
    if len(s1) == 0:
        return True
    if len(s1) == 1:
        return s1 == s2

    for cut in range(1, len(s1)):
        s1_cut1 = s1[:cut]
        s1_cut2 = s1[cut:]
        s1_cut1_sorted = "".join(sorted(s1_cut1))
        s1_cut2_sorted = "".join(sorted(s1_cut2))

        s2_cut1 = s2[:cut]
        s2_cut2 = s2[cut:]
        s2_cut1_sorted = "".join(sorted(s2_cut1))
        s2_cut2_sorted = "".join(sorted(s2_cut2))

        if s1_cut1_sorted == s2_cut1_sorted and s1_cut2_sorted == s2_cut2_sorted:
            are_sub_scrambles = is_scramble(s1_cut1, s2_cut1, memo) and is_scramble(s1_cut2, s2_cut2, memo)
            if are_sub_scrambles:
                memo[key] = True
                return True

        flipped_cut = len(s1) - cut
        s2_cut3 = s2[flipped_cut:]
        s2_cut4 = s2[:flipped_cut]
        s2_cut3_sorted = "".join(sorted(s2_cut3))
        s2_cut4_sorted = "".join(sorted(s2_cut4))
        if s1_cut1_sorted == s2_cut3_sorted and s1_cut2_sorted == s2_cut4_sorted:
            are_sub_scrambles = is_scramble(s1_cut1, s2_cut3, memo) and is_scramble(s1_cut2, s2_cut4, memo)
            if are_sub_scrambles:
                memo[key] = True
                return True

    memo[key] = False
    return False
