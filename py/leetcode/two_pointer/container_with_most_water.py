# You are given an integer array height of length n. There are n vertical lines drawn such that the
# two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the
# most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


class Solution:
    def maxArea(self, height: list[int]) -> int:
        return max_area(height)


def max_area(height: list[int]) -> int:
    start = 0
    end = len(height) - 1
    max_area = 0
    while start < end:
        h_start = height[start]
        h_end = height[end]
        area = min(height[start], height[end]) * (end - start)
        if area > max_area:
            max_area = area

        if h_start <= h_end:
            start += 1
        else:
            end -= 1
    return max_area
