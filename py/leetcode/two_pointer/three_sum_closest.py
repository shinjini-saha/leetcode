# Given an integer array nums of length n and an integer target, find three integers
# at distinct indices in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.
from __future__ import annotations


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        return three_sum_closest(nums, target)


# O(n^2)
def three_sum_closest(nums: list[int], target: int) -> int:
    min_diff: int | None = None
    min_diff_i: tuple[int, int, int] | None = None

    nums = sorted(nums)

    for i, n in enumerate(nums):
        sub_min_diff_i, diff = two_sum_closest(nums, target - n, i)
        if min_diff is None or diff < min_diff:
            min_diff = diff
            min_diff_i = (i, sub_min_diff_i[0], sub_min_diff_i[1])

    if min_diff_i is None or min_diff is None:
        raise Exception()

    i, j, k = min_diff_i
    return nums[i] + nums[j] + nums[k]


# assumes nums is sorted
# returns the two index coordinates and the min diff
def two_sum_closest(nums: list[int], target: int, target_i: int) -> tuple[tuple[int, int], int]:
    min_diff: int | None = None
    min_diff_i: tuple[int, int] | None = None
    start_i = 0
    end_i = len(nums) - 1
    while start_i < end_i:
        if start_i == target_i:
            start_i += 1
            continue
        if end_i == target_i:
            end_i -= 1
            continue
        start_v = nums[start_i]
        end_v = nums[end_i]

        diff = target - (start_v + end_v)
        if diff == 0:
            return (start_i, end_i), 0

        abs_diff = abs(diff)
        if min_diff is None or abs_diff < min_diff:
            min_diff = abs_diff
            min_diff_i = (start_i, end_i)
        if diff < 0:
            end_i -= 1
        else:
            start_i += 1

    if min_diff_i is None or min_diff is None:
        raise Exception()

    return min_diff_i, min_diff
