class Leaderboard:
    """
    1244. Design A Leaderboard

    - heap for the top method.
    - defaultdict for the addScore method
    """

    def __init__(self):
        self.scores = defaultdict(lambda: 0)

    def addScore(self, playerId: int, score: int) -> None:
        if playerId is None or score is None:
            raise Exception(f"Invalid parameters, playerId: {playerId}, score: {score}")
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        if K is None or K == 0:
            raise Exception(f"Invalid parameters, K: {K}")
        if K > len(self.scores):
            K = len(self.scores)
        if K == len(self.scores):
            return sum(self.scores.values())
        """
        k 2
        sums     =  1 7 3 7
        min-heap = [7, 7]
        if len(min-heap) > K then pop the top element
        Time complexity O(nLogK), n is the number of playerIds
        Space Complexity (N + (K + 1))
        """
        min_heap = []
        for v in self.scores.values():
            heapq.heappush(min_heap, v)  # [7 7]
            if len(min_heap) > K:
                heapq.heappop(min_heap)

        return sum(min_heap)

    def reset(self, playerId: int) -> None:
        if playerId is None:
            raise Exception(f"Invalid parameters, playerId: {playerId}")
        if playerId in self.scores:
            del self.scores[playerId]

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)