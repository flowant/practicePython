class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        """
            1152. Analyze User Website Visit Pattern
            https://leetcode.com/problems/analyze-user-website-visit-pattern/description/

            make a website list per user and sort the list

            usera
                        0        1       2       3
            {
                usera: [(a, 0), (b, 2), (c, 3), (d, 4)]
                userb: [(b, 0), (b, 2), (c, 3), (d, 4)]
            }

            make a counter for patterns.
            find a max counter, when counter values are the same, compare website names

            Time Complexity: time complexity of a combination func for the most frequntly visited user
            Space Complexity: the number of unique patterns

        """
        if not username or not timestamp or not website:
            return []

        histories = defaultdict(list)
        for i in range(len(username)):  # 8
            histories[username[i]].append((website[i], timestamp[i]))

        counter = defaultdict(lambda: 0)
        for _, history in histories.items():
            if len(history) < 3:
                continue

            history.sort(key=lambda x: x[1])

            pattern_set = set()
            for pattern in combinations([website for website, timestamp in history], 3):
                pattern_set.add(",".join(pattern))

            for pattern in pattern_set:
                counter[pattern] += 1

        max_count = -1
        max_pattern = None

        for pattern, count in counter.items():
            if max_count == count and pattern < max_pattern:
                max_count = count
                max_pattern = pattern
            elif max_count < count:
                max_count = count
                max_pattern = pattern

        return max_pattern.split(',')
