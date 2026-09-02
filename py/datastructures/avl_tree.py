from __future__ import annotations


class AVLTree:
    def __init__(self):
        self.root: AVLNode | None = None

    def insert(self, val):
        if self.root is None:
            self.root = AVLNode(val)
            return
        self.root = self.root.insert(val)

    def __str__(self):
        return self.root.__str__()


class AVLNode:
    def __init__(self, val: int, left: AVLNode | None = None, right: AVLNode | None = None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 0

    # Returns new root node
    def insert(self, val) -> AVLNode:
        self.insert_only(val)
        self.update_height()

        balance = self.get_balance()
        if -1 <= balance <= 1:
            return self

        if balance < -1:
            return self.handle_left_heavy()
        return self.handle_right_heavy()

    def update_height(self):
        left_height = -1 if self.left is None else self.left.height
        right_height = -1 if self.right is None else self.right.height
        self.height = max(left_height, right_height) + 1

    def insert_only(self, val):
        if val < self.val:
            if self.left is None:
                self.left = AVLNode(val)
            else:
                self.left = self.left.insert(val)
        else:
            if self.right is None:
                self.right = AVLNode(val)
            else:
                self.right = self.right.insert(val)
        self.update_height()

    # -ve means left heavy, positive means right heavy
    def get_balance(self):
        left_height = -1
        if self.left is not None:
            left_height = self.left.height
        right_height = -1
        if self.right is not None:
            right_height = self.right.height

        return right_height - left_height

    # Returns new root node
    def handle_left_heavy(self) -> AVLNode:
        # left heavy - we either have to do a right_rotate or a left_right_rotate
        left = self.left
        if left is None:
            # This shouldn't happen
            return self

        l_balance = self.get_balance()
        if l_balance > 1:
            return self.left_right_rotate()
        else:
            return self.right_rotate()

    # Returns new root node
    def handle_right_heavy(self) -> AVLNode:
        # right heavy - we either have to do a left_rotate or a right_left_rotate
        right = self.right
        if right is None:
            # This shouldn't happen
            return self

        r_balance = right.get_balance()
        if r_balance < 1:
            return self.right_left_rotate()
        else:
            return self.left_rotate()

    # Returns the new root node after the rotation
    def right_rotate(self) -> AVLNode:
        left = self.left
        if left is None:
            return self

        self.left = left.right
        self.update_height()

        left.right = self
        left.update_height()

        return left

    # Returns the new root node after the rotation
    def left_rotate(self) -> AVLNode:
        right = self.right
        if right is None:
            return self

        self.right = right.left
        self.update_height()
        right.left = self
        right.update_height()

        return right

    # Returns the new root node after the rotation
    def left_right_rotate(self) -> AVLNode:
        left = self.left
        if left is not None:
            self.left = left.left_rotate()
            self.update_height()
        return self.right_rotate()

    # Returns the new root node after the rotation
    def right_left_rotate(self) -> AVLNode:
        right = self.right
        if right is not None:
            self.right = right.right_rotate()
        return self.left_rotate()

    def __str__(self):
        strs = get_tree_strings(self)
        s = ""
        for string in strs:
            s = s + "\n" + string
        return s


def get_tree_strings(root: AVLNode) -> list[str]:

    left_strs = get_tree_strings(root.left) if root.left is not None else []
    left_strs2 = (f"    {x}" for x in left_strs)
    right_strs = get_tree_strings(root.right) if root.right is not None else []
    right_strs2 = (f"    {x}" for x in right_strs)

    str_root = f"{root.val}"
    return [*right_strs2, str_root, *left_strs2]
