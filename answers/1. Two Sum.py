class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1. Two Sum
        https://leetcode.com/problems/two-sum/


        nums = [11,15,2,7], target = 9

        use dictionary to keep complements and index of elements.

        complements = 
            # k = target - e, i as a value
            {
                -2: 0,
                -6: 1,
                7: 2,
            }
        """
        if nums is None or len(nums) < 2 or target is None:
            return None
        
        complements = defaultdict(lambda: 0)

        for i, e in enumerate(nums):
            if e in complements:
                return [complements[e], i]
            else:
                complements[target - e] = i
        
        return None


