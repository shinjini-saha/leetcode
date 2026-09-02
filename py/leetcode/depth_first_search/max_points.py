from __future__ import annotations


class Solution:
    def maximumPoints(self, edges: list[list[int]], coins: list[int], k: int) -> int:
        return max_points(edges, coins, k)


class TreeNode:
    def __init__(self, index: int, coins: int, children: list[TreeNode] | None = None):
        self.index = index
        self.coins = coins
        self.children = [] if children is None else children

    def set_coints(self, coins: int):
        self.coins = coins

    def set_children(self, children: list[TreeNode]):
        self.children = children


class Tree:
    def __init__(self, root: TreeNode, max_coin_size: int):
        self.root = root
        self.max_coin_size = max_coin_size

    @classmethod
    def from_arrays(cls, edges: list[list[int]], coins: list[int]):
        nodes = [TreeNode(i, c) for i, c in enumerate(coins)]
        for e_1, e_2 in edges:
            node1 = nodes[e_1]
            node2 = nodes[e_2]
            node1.children.append(node2)
            node2.children.append(node1)

        return Tree(nodes[0], max(coins))


def max_points(edges: list[list[int]], coins: list[int], k: int) -> int:
    tree = Tree.from_arrays(edges, coins)
    return max_points_tree(tree, k)


def max_points_tree(tree: Tree, k: int) -> int:
    memo = {}
    seen = set()

    stack = [(tree.root, "down", 1)]
    while len(stack) > 0:
        node, direction, suppression = stack.pop()

        key = (node.index, suppression)
        if key in memo:
            continue

        available_coins = node.coins // suppression
        max_coin_size_going_forward = tree.max_coin_size // suppression
        should_try_method_1 = max_coin_size_going_forward > 0
        should_try_method_2 = k > 0 and (max_coin_size_going_forward) > 0

        if direction == "down":
            stack.append((node, "up", suppression))
            seen.add(node.index)
            if should_try_method_1 or should_try_method_2:
                for child in node.children:
                    if child.index in seen:
                        continue
                    if should_try_method_1:
                        stack.append((child, "down", suppression))
                    if should_try_method_2:
                        stack.append((child, "down", suppression * 2))
            continue

        if node.index in seen:
            seen.remove(node.index)

        # method 1
        score_meth1 = 0
        if should_try_method_1:
            score_meth1 = available_coins - k
            for child in node.children:
                if child.index in seen:
                    continue
                score_meth1 += memo[(child.index, suppression)]

        # method 2
        score_meth2 = 0
        if should_try_method_2:
            score_meth2 = available_coins // 2
            for child in node.children:
                if child.index in seen:
                    continue
                score_meth2 += memo[(child.index, suppression * 2)]

        memo[key] = max(score_meth1, score_meth2)

    return memo[(0, 1)]
