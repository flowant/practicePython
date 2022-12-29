class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        1823. Find the Winner of the Circular Game

        Josephus problem

        Using DP

        Winner
        n\k  1 2 3 4
         1   1 1 1 1
         2   2 1 2 1
         3   3 3 2 2
         4   4 1 1 2
         5   5 3 4 1

        J(1,k) = 1
        J(n,1) = n
        J(n,k) = J(n-1,k) + k - 1) % n + 1

        Time Complexity = O(n-1)
        Space Complexity = O(1)
        """
        if n == 1:
            return 1
        if k == 1:
            return n

        result = 1  # J(1,k) = 1
        for i in range(2, n + 1):
            """
            i  ((result + k - 1) % i) + 1
            2   (1 + 1) % 2 + 1 = 1
            3   (1 + 1) % 3 + 1 = 3
            4   (3 + 1) % 4 + 1 = 1
            5   (1 + 1) % 5 + 1 = 3
            """
            result = ((result + k - 1) % i) + 1

        return result
