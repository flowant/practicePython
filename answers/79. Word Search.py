class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        79. Word Search

        DFS

        AAA
        AAA
        AAB

        3 * 3 * 3

        Time Complexity: W * 3 ^ L, W is the number of letters in the board, L is the length of input word

        """

        result = False

        if not board or not word:
            return result

        visited = set()
        len_m = len(board)  # 3
        len_n = len(board[0])  # 4

        def _get_adjcent_nodes(m, n, next_letter):  # 0, 0, A
            nonlocal len_m
            nonlocal len_n

            # return adjcent_nodes as a list
            nodes = list()  # [(1, 0), (0, 1)]

            # on the right side
            if n + 1 < len_n and next_letter == board[m][n + 1]:  # 0 < 3 - 1, (0, 1)
                nodes.append((m, n + 1))

            # on the down side
            if m + 1 < len_m and next_letter == board[m + 1][n]:  # 0 < 3 - 1, (1, 0)
                nodes.append((m + 1, n))

            # on the left side
            if n != 0 and next_letter == board[m][n - 1]:
                nodes.append((m, n - 1))

            # on the up side
            if m != 0 and next_letter == board[m - 1][n]:
                nodes.append((m - 1, n))

            return nodes

        def _dfs(m, n, depth):  # 2, 0, 3
            nonlocal result

            if result:
                return

            if depth == len(word):  # 2
                result = True
                return

            visited.add((m, n))

            for next_m, next_n in _get_adjcent_nodes(m, n, word[depth]):  # [(1, 0), (0, 1)]
                if (next_m, next_n) not in visited:
                    _dfs(next_m, next_n, depth + 1)

            visited.remove((m, n))

        for m in range(len_m):
            for n in range(len_n):
                if not result and word[0] == board[m][n]:  # A
                    _dfs(m, n, 1)

        return result
