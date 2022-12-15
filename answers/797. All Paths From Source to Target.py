class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        797. All Paths From Source to Target

        Input: graph = [[1,2],[3, 2],[3],[]]

        - dfs (backtracking)

        Time Complexity: O( (2^(n-2) - 1) * n ), n is the number of nodes.
        Space Complexity: O(n), the max length of track_list is n

        """

        if not graph:
            return []

        result = list()  # [[0 1 3] [0 1 2 3] [0 2 3]]
        track_list = list()
        target_node = len(graph) - 1

        def _dfs(node):
            track_list.append(node)  # [0 2 3]

            if node == target_node:
                result.append(deepcopy(track_list))
                track_list.pop()
                return

            for adjacent_node in graph[node]:  # 1 2
                _dfs(adjacent_node)

            track_list.pop()

        _dfs(0)

        return result
