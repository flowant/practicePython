class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        611. Valid Triangle Number

        Input: nums = [1,2,3,4,5]

        - sort input
        - index_a < index_b < index_c

         0 1 2 3 4
        [1,2,3,4,5]
           a b   c

           2, 4, 5
           3, 4, 5
          2 3 5

        result += index_b - index_a

        Time Complexity: O(n^2)
        Space Complexity: space complexity of sort() method.

        """
        if not nums or len(nums) < 3:
            return 0

        nums.sort()
        result = 0

        for index_c in range(2, len(nums)):  # 2
            index_a = 0  # 0
            index_b = index_c - 1  # 1
            while index_a < index_b:
                if nums[index_a] + nums[index_b] > nums[index_c]:
                    result += index_b - index_a  # 1
                    index_b -= 1
                else:
                    index_a += 1

        return result