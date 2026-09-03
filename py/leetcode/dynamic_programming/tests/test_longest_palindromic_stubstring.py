from leetcode.dynamic_programming.longest_palindromic_stubstring import longest_palindrome


def test_longest_palindrome():
    assert longest_palindrome("babad") == "bab"  # or aba
    assert longest_palindrome("bb") == "bb"
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("cbvbd") == "bvb"
    assert longest_palindrome("zeusnillinsue") == "eusnillinsue"
    assert longest_palindrome("abbcccbbbcaaccbababcbcabca") == "bbcccbb"
    assert (
        longest_palindrome("zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez")
        == "zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez"
    )
