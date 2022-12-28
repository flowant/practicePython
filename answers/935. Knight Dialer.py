class Solution:
    def knightDialer(self, n: int) -> int:
        """
        935. Knight Dialer

        Use DP, calculate the count of paths from the right most digit.

        n 1   |   > 2             | 2  | 3

        count_path
        cp1 1 | = cp6 + cp8       | 2  | 5   (n=2, 61, 81) (n=3, 161, 761, 061, 181 381)
        cp2 1 | = cp7 + cp9       | 2  | 4
        cp3 1 | = cp4 + cp8       | 2  | 5
        cp4 1 | = cp3 + cp9 + cp0 | 3  | 6
        cp5 1 |                   | 0  | 0
        cp6 1 | = cp1 + cp7 + cp0 | 3  | 6
        cp7 1 | = cp2 + cp6       | 2  | 5
        cp8 1 | = cp1 + cp3       | 2  | 4
        cp9 1 | = cp2 + cp4       | 2  | 5
        cp0 1 | = cp4 + cp6       | 2  | 6

        sum 10                      20   46

        Time, Space complexity = O(n)

        """
        mod = 10 ** 9 + 7
        if not n:
            return 0

        count_path = [1] * 10

        while n > 1:  # 1
            count_path = [
                # new_count_path[0] = prev_count_path[4] + prev_count_path[6]
                count_path[4] + count_path[6],
                count_path[6] + count_path[8],
                count_path[7] + count_path[9],
                count_path[4] + count_path[8],
                count_path[3] + count_path[9] + count_path[0],
                # count_path[5] has fixed value 0 when n > 1
                0,
                count_path[1] + count_path[7] + count_path[0],
                count_path[2] + count_path[6],
                count_path[1] + count_path[3],
                count_path[2] + count_path[4],
            ]
            n -= 1

        return sum(count_path) % mod

