# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

from __future__ import annotations


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return longest_valid_parentheses(s)


class Layer:
    def __init__(self, start_idx: int, end_idx: int | None = None, parent: Layer | None = None):
        self.start_idx = start_idx
        self.end_idx: None | int = end_idx
        self.parent = parent
        self.next: list[Layer] = []

    def length(self):
        if self.end_idx is None:
            return 0
        return self.end_idx - self.start_idx + 1

    def __str__(self):
        return f"start_idx: {self.start_idx}, end_idx: {self.end_idx}, parent: {self.parent.start_idx if self.parent is not None else None}, next: {len(self.next)}"


def longest_valid_parentheses(s: str) -> int:
    if s == "":
        return 0

    roots: list[Layer] = []
    current_layer: Layer | None = None
    max_length = 0
    for i, paren in enumerate(s):
        if paren == "(":
            new_layer = Layer(i, parent=current_layer)

            if current_layer is not None:
                current_layer.next.append(new_layer)
            else:
                roots.append(new_layer)
            current_layer = new_layer
        else:
            if current_layer is None:
                continue
            current_layer.end_idx = i
            current_layer.next.clear()
            current_layer = current_layer.parent

            if current_layer is not None:
                children_length = sum([c.length() for c in current_layer.next])
                if children_length > max_length:
                    max_length = children_length

    children_length = get_root_max_length(roots)
    if children_length > max_length:
        max_length = children_length

    return max_length


def get_root_max_length(roots: list[Layer]) -> int:
    combined = []
    max_length = 0
    for root in roots:
        prev = combined[-1] if len(combined) > 0 else None
        if prev is not None and prev.end_idx is not None and prev.end_idx + 1 == root.start_idx:
            combined.pop()
            combined_root = Layer(prev.start_idx, root.end_idx)
            combined.append(combined_root)
            length = combined_root.length()
            if length > max_length:
                max_length = length
            continue

        combined.append(root)
        length = root.length()
        if length > max_length:
            max_length = length

    return max_length
