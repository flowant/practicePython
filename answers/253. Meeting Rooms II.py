import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        253. Meeting Rooms II
        https://leetcode.com/problems/meeting-rooms-ii/

        Input: intervals = [[0,30],[5,10],[15,20]]
        Output: 2

        - Sort lists using start time
        - add the first end time to min heap.
        - if heap[0] is smaller then or equals to next start time, then pop and push the end time
          else just push end time
        - return len(heap) after the interation

        [20, 30]

        Time complexity O(nlogn)
        Space complexity O(n)
        """

        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])  # [[0,30],[5,10],[15,20]]

        min_heap = [intervals[0][1]]  # [20, 30]

        for i in range(1, len(intervals)):  # 1
            if min_heap[0] <= intervals[i][0]:  # 10 < 15
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, intervals[i][1])

        return len(min_heap)
