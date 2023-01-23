class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        3. Longest Substring Without Repeating Characters

        Input: s = "abcabcbb"
                      l
                        r

        Output: 3

        character_set = {c a b}

        removed chracter = b

        1. in loop, add a character at index R if the character is not in a set
        - if a character is in the set
        +- update max_len
        +- in inner loop remove a character at index L, and save the removed character
        +- increase index l
        +- if the removed character is same as the character at r exit inner loop.


        max_len = 0

        max_len = max(max_len, len(character_set))
        """

        if not s:
            return 0
        len_s = len(s)
        if len_s == 1:
            return 1

        max_len = 0  # 3
        char_set = set()
        index_left = 0
        index_right = 0

        # "abcabcbb"
        #  01234567
        #         l
        #          r
        #  {  b   }
        while index_right <= len_s:
            if index_right == len_s:
                max_len = max(max_len, len(char_set))
                break
            elif s[index_right] in char_set:
                max_len = max(max_len, len(char_set))
                while index_left < index_right:
                    char_set.remove(s[index_left])
                    removed_character = s[index_left]  # b
                    index_left += 1
                    if removed_character == s[index_right]:
                        break
            else:
                char_set.add(s[index_right])
                index_right += 1

        return max_len
