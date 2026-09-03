# Given an array of integers nums and an integer target, return indices of the two numbers such that they
# add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return two_sum(nums, target)


def two_sum(nums: list[int], target: int) -> list[int]:
    nums_with_indices = []
    for i, v in enumerate(nums):
        nums_with_indices.append((v, i))
    sorted_nums = sorted(nums_with_indices)
    start_i = 0
    end_i = len(sorted_nums) - 1
    while start_i < end_i:
        start_val, start_old_index = sorted_nums[start_i]
        end_val, end_old_index = sorted_nums[end_i]
        total = start_val + end_val

        if total == target:
            return [start_old_index, end_old_index]
        if total < target:
            start_i += 1
            continue
        end_i -= 1

    return []


def two_sum_hash(nums: list[int], target: int) -> list[int]:
    hash: dict[int, int] = {}
    for i, n in enumerate(nums):
        if n in hash:
            other_i = hash[n]
            return [i, other_i]
        diff = target - n
        hash[diff] = i
    return []
