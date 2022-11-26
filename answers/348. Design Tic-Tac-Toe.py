class TicTacToe:
    """
    348. Design Tic-Tac-Toe
    https://leetcode.com/problems/design-tic-tac-toe/description/

    using counter per row and column and diagonal and anti-diagonal
    when counter value is either 3 or -3, the player calling move win.

    Input
        ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
        [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
        Output
        [null, 0, 0, 0, 0, 0, 0, 1]

        couters
        d:2   c0:1  c1:1   c2:-1 anti-d:0
        r0:0 |  1          -1
        r1:-2| -1          -1
        r2:3 |  1     1     1

    Time Complexity: O(1)
    Space Complexity: O(2n + 2)

    """

    def __init__(self, n: int):
        self.n = n
        self.counter_row = [0] * n
        self.counter_column = [0] * n
        self.counter_diagonal = 0
        self.counter_anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        delta = 1 if player == 1 else -1

        self.counter_row[row] += delta
        self.counter_column[col] += delta
        if row == col:
            self.counter_diagonal += delta
        if self.n - 1 - row == col:
            self.counter_anti_diagonal += delta

        if abs(self.counter_row[row]) == self.n \
                or abs(self.counter_column[col]) == self.n \
                or abs(self.counter_diagonal) == self.n \
                or abs(self.counter_anti_diagonal) == self.n:
            return player
        else:
            return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
