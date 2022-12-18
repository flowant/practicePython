class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        1347. Minimum Number of Steps to Make Two Strings Anagram

        Input: s = "leetcode", t = "practice"
        Output: 5

        Input: s = "leode", t = "praic"
        counters {
            l: 1
            e: 2
            t: 0
            c: -1
            o: 1
            d: 1
            p: -1
            r: -1
            a: -1
            i: -1
        }

        increase counter for a letter in s,
        decrease counter for a letter in t

        return the sum of counters which are grater than 0

        Time, Space Complexity = O(n)
        """
        if not s or not t or len(s) != len(t):
            return 0

        counters = defaultdict(lambda: 0)

        for letter in s:
            counters[letter] += 1

        for letter in t:
            counters[letter] -= 1

        result = 0
        for v in counters.values():
            if v > 0:
                result += v

        return result
