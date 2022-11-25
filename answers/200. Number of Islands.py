class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        200. Number of Islands
        https://leetcode.com/problems/number-of-islands/description/

        Input: grid = [
        ["V","V","0","0","0"],
        ["V","V","0","0","0"],
        ["0","0","V","0","0"],
        ["0","0","0","V","V"]
        ]
        Output: 3

        Find the number of connected components using DFS

        land_count # 1 2 3

        len_rows = len(grid)  # 4
        len_columns = len(grid[0])  # 5

        land_count = 0

        for index_row in range(len_rows):
            for index_column in range(len_columns):
                if grid[index_row][index_column] == "1"
                    land_count += 1
                    DFS(index_row, index_column)

        DFS(index_row, index_column):
            grid[index_row][index_column] = "V"

            # To the top element
            if index_row != 0 and grid[index_row - 1][index_column] == "1":
                DFS(index_row - 1,index_column)

            # To the bottom element
            if index_row != len_rows - 1 and grid[index_row + 1][index_column] == "1":
                DFS(index_row + 1,index_column)

            # To the right element
            if index_column != len_column - 1 and grid[index_row][index_column + 1] == "1":
                DFS(index_row, index_column + 1)

            # To the left element
            if index_column != 0 and grid[index_row][index_column - 1] == "1"
                DFS(index_row, index_column - 1)

        Time Complexity: O(len_rows*len_column*2)
        """

        if not grid or not grid[0]:
            return 0

        len_rows = len(grid)  # 4
        len_columns = len(grid[0])  # 5

        def DFS(index_row, index_column):
            grid[index_row][index_column] = "V"

            # To the top element
            if index_row != 0 and grid[index_row - 1][index_column] == "1":
                DFS(index_row - 1, index_column)

            # To the bottom element
            if index_row != len_rows - 1 and grid[index_row + 1][index_column] == "1":
                DFS(index_row + 1, index_column)

            # To the right element
            if index_column != len_columns - 1 and grid[index_row][index_column + 1] == "1":
                DFS(index_row, index_column + 1)

            # To the left element
            if index_column != 0 and grid[index_row][index_column - 1] == "1":
                DFS(index_row, index_column - 1)

        land_count = 0
        for index_row in range(len_rows):
            for index_column in range(len_columns):
                if grid[index_row][index_column] == "1":
                    land_count += 1
                    DFS(index_row, index_column)

        return land_count
