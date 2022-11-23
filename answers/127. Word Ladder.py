class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        127. Word Ladder
        https://leetcode.com/problems/word-ladder/description/

        input =
        ["hot","dot","dog","lot","log","cog"]

        output = 5

        adjacent_map = {
            "*ot": ["hot", "dot", "lot"]
            "h*t": ["hot"]
            "ho*": ["hot"]
        }

        visited = set("hot")

        BFS // O(n)

        Initialise Queue [6]
        """

        word_len = len(beginWord)

        adjacent_map = defaultdict(list)
        for word in wordList:
            for i in range(word_len):
                word_pattern = word[:i] + "*" + word[i + 1:] # time, space complexity: O(word_len ^2 * n)
                adjacent_map[word_pattern].append(word)

        visited = set()

        from queue import Queue
        q = Queue(len(wordList) + 1)
        q.put((beginWord, 1))
        visited.add(beginWord)

        while not q.empty():
            word, depth = q.get()

            if word == endWord:
                return depth

            for i in range(word_len):
                word_pattern = word[:i] + "*" + word[i + 1:] # O(word_len ^2)
                for adj_word in adjacent_map[word_pattern]:
                    if adj_word not in visited:
                        q.put((adj_word, depth + 1))  # # O(word_len ^2 * n)
                        visited.add(adj_word)
                adjacent_map[word_pattern] = []

        return 0
