# You are given a string s. You can convert s to a palindrome by adding characters in front of it.

# Return the shortest palindrome you can find by performing this transformation.

import string


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        return shortest_palindrome(s)


def shortest_palindrome(s: str) -> str:
    if s == "":
        return s
    memo = [[]] * len(s)
    for i in range(len(s) // 2, 0, -1):
        expand_palindromes_starting_at(i, s, memo)
    expand_palindromes_starting_at(0, s, memo, True)
    largest_palindrome_end_i = memo[0][0]
    if largest_palindrome_end_i == len(s) - 1:
        return s
    new_s = s
    for i in range(largest_palindrome_end_i + 1, len(s)):
        new_s = s[i] + new_s

    return new_s


# We will expand going backwards
def expand_palindromes_starting_at(i: int, s: str, memo: list[list[int]], max_only=False):
    # Note: Based on how this is constructed, the list of palindromes ends up being sorted
    if i == len(s) - 1:
        memo[i] = [i]
        return

    val = s[i]
    prev_palindromes = memo[i + 1]
    # we can clean up memory after using it
    memo[i + 1] = []

    new_palindromes = []
    for s_i in prev_palindromes:
        if s_i == len(s) - 1:
            continue
        new_s_val = s[s_i + 1]
        if new_s_val != val:
            continue
        new_palindromes.append(s_i + 1)
        if max_only:
            break

    if s[i + 1] == s[i]:
        new_palindromes.append(i + 1)
    new_palindromes.append(i)
    memo[i] = new_palindromes


def shortest_palindrome_hash_cal(s: str) -> str:
    if len(s) <= 1:
        return s

    BASE = len(string.ascii_letters) + 1
    MOD_PRIME = 10**9 + 7

    LETTER_TO_INDEX = {letter: i + 1 for (i, letter) in enumerate(string.ascii_letters)}

    forward_hash = 0
    backward_hash = 0

    longest_palindrome_i = 0

    count = 0
    base_power = 1
    for i in range(len(s)):
        count += 1
        letter = s[i]
        letter_i = LETTER_TO_INDEX[letter]
        # a b c
        # forward => a * B**2 + b * B**1 + c * B**0 => forward(n-1)*B + c
        # backward => a * B**0 + b * B**1 + c * B**2 => backward(n-1) + c*B**pow
        forward_hash = (forward_hash * BASE + letter_i) % MOD_PRIME
        if i > 0:
            base_power = (base_power * BASE) % MOD_PRIME
        backward_hash = (backward_hash + letter_i * base_power) % MOD_PRIME

        if forward_hash == backward_hash:
            longest_palindrome_i = i
    if longest_palindrome_i == len(s) - 1:
        return s
    return s[longest_palindrome_i + 1 : len(s)][::-1] + s


# def is_palindrome(s: str) -> bool:
#     for i in range(len(s)//2):
#         if s[i] != s[len(s)-1-i]:
#             return False
#     return True
