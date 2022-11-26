from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        239. Sliding Window Maximum
        https://leetcode.com/problems/sliding-window-maximum/description/

        Explanation:
        Window position                Max
        ---------------               -----
        0  1  2   3  4  5  6  7
        [1  3  -1]3  1  3  6  7       3
        1 [3  -1  3] 1  3  6  7       3
        1  3 [-1  3  1] 3  6  7       3
        1  3  -1 [3  1  3] 6  7       3
        1  3  -1  3 [1  3  6] 7       6
        1  3  -1  3  1 [3  6  7]      7

        k = 2
        index 0  1  2  3
        value 1  1  1  1

        Use deque
        - remove index from window, remove index <= i - k (2 - 2) 0
        - remove indices having values smaller than or equals to the value to be added.
          A left emement in dq is always greater than the right element of it.
        - dq[0] is the current max in the window, add the dq[0] since i >= k - 1 (1)

        index [0   1] 2
        value [4 > 3] 2

        result = 1 1 1

        Time complexity: O(n)
        Space complexity: O(n + k)

        """

        if not nums or not k or k == 0:
            return []

        if k == 1:
            return nums

        len_nums = len(nums)
        dq = deque()
        result = list()

        for i in range(len_nums):
            if dq and dq[0] <= i - k:  # 2 <= 3 - 2
                dq.popleft()
            while dq and nums[dq[-1]] <= nums[i]:  #
                dq.pop()
            dq.append(i)  # index 2
            # value 1
            if i >= k - 1:  # 1 >= 1
                result.append(nums[dq[0]])

        return result  # [1, 1, 1]
