class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        """
        2038. Remove Colored Pieces if Both Neighbors are the Same Color

                         0123456
        Input: colors = "AAABABB"
        Output: true

        Count "AAA" and "BBB". If the count of "AAA" is grater than the other, Alice win


        """
        count_aaa = 0
        count_bbb = 0

        for i in range(len(colors) - 2):  # 7 - 2 = 5
            slice = colors[i:i + 3]
            if slice == "AAA":
                count_aaa += 1
            elif slice == "BBB":
                count_bbb += 1

        return count_aaa > count_bbb
