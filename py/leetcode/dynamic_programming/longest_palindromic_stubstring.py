# Given a string s, return the longest palindromic substring in s.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return longest_palindrome(s)


def longest_palindrome(s: str) -> str:
    # palindromes ending at index i (save start i; end i is just the index)
    memo = []
    return longest_palindrome_helper(s, memo)


def longest_palindrome_helper(s: str, memo: list[list[int]]) -> str:
    if s == "":
        return ""
    longest_palindrome = (0, 0)
    longest_palindrome_size = 1
    for i in range(len(s)):
        expand_palindromes_ending_at(i, s, memo)
        palindromes_at_i = memo[i]
        largest_pal_start_i = palindromes_at_i[0]
        size = i - largest_pal_start_i + 1
        if size > longest_palindrome_size:
            longest_palindrome = (largest_pal_start_i, i)
            longest_palindrome_size = size

    return s[longest_palindrome[0] : longest_palindrome[1] + 1]


def expand_palindromes_ending_at(i: int, s: str, memo: list[list[int]]):
    # Note: Based on how this is constructed, the list of palindromes ends up being sorted
    if i == 0:
        memo.append([0])
        return

    val = s[i]
    prev_palindromes = memo[i - 1]

    # we can clean up memory after using it
    memo[i - 1] = []

    new_palindromes = []
    for s_i in prev_palindromes:
        if s_i == 0:
            continue
        new_s_val = s[s_i - 1]
        if new_s_val != val:
            continue
        new_palindromes.append(s_i - 1)

    if s[i - 1] == s[i]:
        new_palindromes.append(i - 1)
    new_palindromes.append(i)
    memo.append(new_palindromes)
