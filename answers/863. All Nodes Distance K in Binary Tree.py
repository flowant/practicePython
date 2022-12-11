# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        863. All Nodes Distance K in Binary Tree

        - by adding parent point, create graph structure
        - BFS

        Time, Space complexity: O(n)
        """
        if not root:
            return []

        def _dfs_add_parent(node: TreeNode):  # 3 | 5 |6
            for child in [node.left, node.right]:  # 5.p=3 1.p=3 6.p = 5 2.p =5
                if child:
                    child.parent = node
                    _dfs_add_parent(child)

        root.parent = None
        _dfs_add_parent(root)

        result = list()  # 1
        visited = set()

        dq = deque([(target, 0)])  #
        visited.add(target)  # 3

        while dq:
            node, depth = dq.pop()  # (3, 0)
            if depth == k:
                result.append(node.val)
            else:
                for adjacent_node in [node.parent, node.left, node.right]:
                    if adjacent_node and adjacent_node not in visited:
                        dq.appendleft((adjacent_node, depth + 1))
                        visited.add(adjacent_node)

        return result
