# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        314. Binary Tree Vertical Order Traversal

        Input: root = [3,9,20,null,null,15,7]
        Output: [[9],[3,15],[20],[7]]

        BFS,

                3
            9       20
                15       7

        [(7, 2)(15, 0)](20, 1)

        push left child into pop with decreased column index, push right child...
        min_column_index = -1
        max_column_index = 1

        defaultdict(list) {
            0: [3, 15]
            1: [20]
            -1: [9]
            2: [7]
        }

        """
        if not root:
            return []

        dq = deque([(root, 0)])
        min_column_index = 0
        max_column_index = 0
        column_nodes = defaultdict(list)

        while dq:  # [(7, 2)|(15, 0)|(20, 1)|(9, -1)(3, 0)]
            node, column_index = dq.pop()
            column_nodes[column_index].append(node.val)
            if node.left:
                dq.appendleft((node.left, column_index - 1))
            if node.right:
                dq.appendleft((node.right, column_index + 1))
            min_column_index = min(min_column_index, column_index)  # -1
            max_column_index = max(max_column_index, column_index)  # 2

        result = list()
        for i in range(min_column_index, max_column_index + 1):
            result.append(column_nodes[i])
        # [[9], [3, 15], [20], [7]]

        return result
