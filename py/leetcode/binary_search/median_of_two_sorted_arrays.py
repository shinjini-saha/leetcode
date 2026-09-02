# Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
from __future__ import annotations

import math


class Solution:
    def findMedianSortedArrays(self, l1: list[int], l2: list[int]) -> float:
        return find_median_sorted_arrays(l1, l2)


# Returns the list with the larger size first
def order_larger_then_smaller(l1: list[int], l2: list[int]):
    if len(l1) >= len(l2):
        return l1, l2
    return l2, l1


def find_median_sorted_arrays(l1: list[int], l2: list[int]) -> float:
    total_size = len(l1) + len(l2)

    l1, l2 = order_larger_then_smaller(l1, l2)

    l1_cut_lo = 0
    l1_cut_hi = len(l1)
    while l1_cut_lo <= l1_cut_hi:
        l1_cut = (l1_cut_lo + l1_cut_hi) // 2
        l2_cut = total_size // 2 - l1_cut

        l1_l = get_val(l1, l1_cut - 1)
        l1_r = get_val(l1, l1_cut)

        l2_l = get_val(l2, l2_cut - 1)
        l2_r = get_val(l2, l2_cut)

        if l2_r < l1_l:
            # cut too far to the right
            l1_cut_hi = (l1_cut_lo + l1_cut_hi) // 2
        elif l1_r < l2_l:
            # cut too far to the left
            l1_cut_lo = (l1_cut_lo + l1_cut_hi) // 2
            if l1_cut_lo == (l1_cut_lo + l1_cut_hi) // 2:
                l1_cut_lo += 1
        else:
            return get_median(max(l1_l, l2_l), min(l1_r, l2_r), total_size)

    raise Exception()


def get_val(items: list[int], i: int):
    if i < 0:
        return -math.inf
    if i >= len(items):
        return math.inf
    return items[i]


def get_median(left: int | float, right: int | float, total_size: int):
    if total_size % 2 == 1:
        return right
    # Use this form to reduce chance of value overflowing before divide
    return right + (left - right) / 2
