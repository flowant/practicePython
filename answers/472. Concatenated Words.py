class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        472. Concatenated Words
        https://leetcode.com/problems/concatenated-words/description/

        Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
        Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

        - wordSet = set(words)

        for each word,
        is_concatable = [False] * len + 1
        is_concatable[0] = True
        is_concatable[n] value is True when the length n substring (word[:n]) consists valid prefix, suffix .
        prefix, n is smaller than len(word): any combination of words in wordSet including Empty string.
        prefix, n equals to len(word): any combination of words in wordSet excluding Empty string.
        suffix: a word in wordSet.

        #  0 1 2 3 4 5 6 7 8 9 10 11 (length of substring of word)
           T F F T T F F T F F T  T

                    i
         012345678901
        "catsdogcats"
          j

        if is_concatable[-1]:
            result.append(word)

        Time complexity: O(N * M^2) N is the length of words, M is the maximum length of words
        Space complexity: O(N*M + M + 1)
        """
        if not words:
            return []

        wordSet = set(words)

        result = list()

        for word in words:  # "catsdogcats"
            len_word = len(word)  # 11
            is_concatable = [False] * (len_word + 1)  # 0 ~ 11
            is_concatable[0] = True

            for i in range(1, len_word + 1):
                for j in range(0 if i != len_word else 1, i):  # j
                    if is_concatable[i]:
                        break
                    if is_concatable[j] and word[j:i] in wordSet:  # c
                        is_concatable[i] = True

            if is_concatable[-1]:
                result.append(word)

        return result
