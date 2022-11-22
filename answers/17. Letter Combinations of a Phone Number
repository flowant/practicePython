class Solution:
    button_chars = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }

    def letterCombinations(self, digits: str) -> List[str]:
        """
        17. Letter Combinations of a Phone Number
        https://leetcode.com/problems/letter-combinations-of-a-phone-number/


        "23", time & space complexity: O(4^n),

         a                 b                 c
         ad          e     f     d     e     f     d     e     f
         adg adh adi g h i g h i g h i g h i g h i g h i g h i g h i


                  "3"    "a"            ['ad', 'ae', 'af']
        combinate(digits, combinations, result)
            chars = map[digits[0]]
            for c in chars:  #  def
                if len(digit) == 1:
                    result.append(combinations + c)
                else:
                    combinate(digits[1:], combinations + c, result) # 3, "a", []
        """
        result = list()

        Solution.combinate(digits, "", result)

        return result

    @staticmethod
    def combinate(digits, combinations, result):
        if digits is None or len(digits) == 0:
            return []

        chars = Solution.button_chars.get(digits[0], "")
        for c in chars:
            if len(digits) == 1:
                result.append(combinations + c)
            else:
                Solution.combinate(digits[1:], combinations + c, result)
