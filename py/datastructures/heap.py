import math


class MinHeap:
    def __init__(self):

        # [a, al, ar, all, alr, arl, arr, alll, allr, alrl, alrr]
        # [0,  1,  2,   3,   4,   5,   6,    7,    8,    9,   10]
        self.array: list[int] = []

    def get_left_child_index(self, i: int) -> int:
        return (i * 2) + 1

    def get_right_child_index(self, i: int) -> int:
        return (i * 2) + 2

    def get_parent_index(self, i: int) -> int:
        return math.floor((i - 1) / 2)

    def get_left_child(self, i: int) -> int | None:
        child_idx = self.get_left_child_index(i)
        return self.get_value(child_idx)

    def get_right_child(self, i: int) -> int | None:
        child_idx = self.get_right_child_index(i)
        return self.get_value(child_idx)

    def get_parent(self, i: int) -> int | None:
        parent_idx = self.get_parent_index(i)
        return self.get_value(parent_idx)

    def get_value(self, i: int) -> int | None:
        if i < 0 or i >= len(self.array):
            return None
        return self.array[i]

    def insert(self, new_val) -> None:
        # insert at the end and then heapify up
        self.array.append(new_val)
        self.heapify_up(len(self.array) - 1)

    # parent_idx is parent index
    # it checks if the parent is smaller than its children and if not, swaps it with the smaller child
    def heapify_down(self, parent_idx):
        if parent_idx == len(self.array) - 1:
            return

        val = self.get_value(parent_idx)
        if val is None:
            return

        child_l_idx = self.get_left_child_index(parent_idx)
        child_l = self.get_left_child(parent_idx)
        child_r_idx = self.get_right_child_index(parent_idx)
        child_r = self.get_right_child(parent_idx)

        if (child_l is None or val < child_l) and (child_r is None or val < child_r):
            return

        min_child_idx = self.get_min_child(child_l_idx, child_r_idx)

        if min_child_idx is not None:
            self.array[min_child_idx], self.array[parent_idx] = (
                self.array[parent_idx],
                self.array[min_child_idx],
            )
            self.heapify_down(min_child_idx)

    def get_min_child(
        self,
        child_l_idx: int,
        child_r_idx: int,
    ) -> int:
        child_l = self.get_value(child_l_idx)
        child_r = self.get_value(child_r_idx)
        if child_l is None:
            return child_r_idx
        if child_r is None:
            return child_l_idx

        min_child = child_l
        min_child_idx = child_l_idx
        if min_child > child_r:
            min_child = child_r
            min_child_idx = child_r_idx
        return min_child_idx

    # child_idx is child index
    # it checks if the parent is smaller than child and if not, swaps
    def heapify_up(self, child_idx):
        if child_idx == 0:
            return

        val = self.get_value(child_idx)
        if val is None:
            return
        parent_idx = self.get_parent_index(child_idx)
        parent_val = self.get_parent(child_idx)

        if parent_val is not None and parent_val > val:
            self.array[parent_idx], self.array[child_idx] = (
                self.array[child_idx],
                self.array[parent_idx],
            )
            self.heapify_up(parent_idx)

    def pop(self) -> None | int:
        if len(self.array) == 0:
            return None
        min_val = self.array[0]
        self.array[0] = self.array[len(self.array) - 1]
        self.array.pop()
        self.heapify_down(0)
        return min_val

    def __str__(self):
        return str(self.array)
