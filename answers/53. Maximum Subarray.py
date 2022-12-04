class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        53. Maximum Subarray

        Input: nums =               [-2, 1,-3, 4,-1, 2, 1,-5, 4]
        Output: 6

        - max_sum_subarray + num     -2 -1 -2  2  3  5  6  1  5
        - max of the above and num   -2  1 -2  4  3  5  6  1  5
        - max of the above           -2  1  1  4  4  5  6  6  6
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        max_sum_subarray = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            max_sum_subarray = max(max_sum_subarray + num, num)
            max_sum = max(max_sum_subarray, max_sum)

        return max_sum
