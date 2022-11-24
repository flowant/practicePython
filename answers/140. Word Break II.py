class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        140. Word Break II
        https://leetcode.com/problems/word-break-ii/description/

        Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
        Output: ["cats and dog", "cat sand dog"]

        len_s=N, len_words=W

        "catsanddog"  [[cat sand dog], [cats and dog]]
        set{"cat","cats","and","sand","dog"}                  // N * O(1)

        break_down(s) return [[cat sand dog] [cats and dog]]

        cat.sanddog [[cat sand dog]]  cats.anddog       [[cats and dog]]                  catsa x
        sand.dog                      and.dog           [[and, dog]]
        dog.                          dog.              [[dog]]
        ""                            ""                [[]]

        #Time complexity
        - make wordSet: W, the number of words from input
        - call _break_down: 1 + 2 + 3 +.. N = (1 + N)N/2 = O(N^2)
        - make result: 1, 2, 4, 8 = O(2^n)

        # worst case
        s = aaaa
        set{"a","aa","aaa","aaaa"}

        aaaa [[a a a a] [a a aa] [a aa a] [a aaa] [aa a a] [aa aa] [aaa a] [aaaa]] = 8 inner lists, 2^(n-1) * n
        a.aaa aa.aa    aaa.a   aaaa. N

        aaa [[a a a] [a aa] [aa a] [aaa]] = 4, 2^(n-2) * n-1
        a.aa   aa.a   aaa

        aa [[a a] [aa]]
        a.a       aa.

        a [[a]]
        a.

        #Space complexity
        - results: 2^(n-1) * n
        - wordSet: W

        """

        if not s or not wordDict:
            return []

        wordSet = set(wordDict)  # O(W)

        results = defaultdict(list)  # {}

        def _break_down(s):  # catsanddog
            if not s:
                return [[]]

            if s in results:
                return results[s]

            for i in range(1, len(s) + 1):
                prefix = s[:i]
                if prefix in wordSet:
                    # [[sand, dog], [...]] -> [[cat, sand, dog] [cat ...]]
                    results[s] += [[prefix] + words for words in _break_down(s[i:])]
                    # _break_down actually calculates X times. X is the number of all unique suffixes.

            return results[s]

            # _break_down(catsanddog) [[cat, sand, dog]]     [[cats, and, dog]]
            # p=cat                                     p=cats
            # _break_down(sanddog) [[sand, dog]]        _break_down(anddog) [[and, dog]]
            # p=sand                                    p=and
            # _break_down(dog) [[dog]]                  _break_down(dog) [[dog]]
            #                            p=dog (memoization) [[dog]]
            #                            _break_down("") -> [[]]

        _break_down(s)

        # [[cat, sand, dog], [cats, and, dog]] to ["cat sand dog", "cats and dog"]
        return [" ".join(word_list) for word_list in results[s]]
