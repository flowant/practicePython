class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        """
        1583. Count Unhappy Friends

        Input: n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]],
        pairs = [[0, 1], [2, 3]]
        Output: 2

        prefer_over_paired = {
            0: {}
            1: {3, 2}
            2: {}
            3: {1}
        }

        for person(x), friends_prefered_over_paired in prefer_over_paired.items():
            for friend(u) in friends_prefered_over_paired:
                if person in prefer_over_paired[friend]:
                    count_unhappy +=1
                    break

        Time, Space Complexity: O(n^2)
        """
        if n is None or not preferences or not pairs:
            raise Exception(f"Invalid parameters n:{n}, preferences:{preferences}, pairs:{pairs}")

        prefer_over_paired = defaultdict(set)
        count_unhappy = 0

        for paired_a, paired_b in pairs:  # 2, 3
            for prefered_friend in preferences[paired_a]:  # [3, 1, 0]
                if prefered_friend == paired_b:  # 3 3
                    break
                prefer_over_paired[paired_a].add(prefered_friend)

            for prefered_friend in preferences[paired_b]:  # [1, 2, 0]
                if prefered_friend == paired_a:  # 1 != 2
                    break
                prefer_over_paired[paired_b].add(prefered_friend)

        """
            [[1,3,2],[2,3,0],[1,3,0],[0,2,1]]
            [[1,3],[0,2]]

            prefer_over_paired = {
            0:{1, 3}
            1:{2}
            2:{1, 3}
            3:{0,2}
        }
        """
        for person, friends_prefered_over_paired in prefer_over_paired.items():  # 3
            for friend in friends_prefered_over_paired:  # 1
                if friend in prefer_over_paired and person in prefer_over_paired[friend]:  # 3
                    count_unhappy += 1  # 2
                    break

        return count_unhappy