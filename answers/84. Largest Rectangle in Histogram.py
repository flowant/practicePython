class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        84. Largest Rectangle in Histogram
        https://leetcode.com/problems/largest-rectangle-in-histogram/description/

        use monotonic incresing stack:
        - bottom side elements are always smaller than top side elements.
        - when the stack has only one element, the element is min value among elements from first to current iteration.
        - to push new value, pop until new value is greater than the top value.
          during poping value, calculate max the area.

        Input: heights = [2,1,5,6,2,3]
        Output: 10

        append 0 to the input list to make the last element from input smaller than 0

        index: 0 1 2 3 4 5 6
        v     [2,1,5,6,2,3,0]

        stack:
        index  0
        height 2

        iteration: 0
        hegith: 2

        poped: 0 at index 2

        Time, Space Complexities: O(n)
        """
        if not heights:
            return 0

        mono_inc_stack = list()
        heights.append(0)
        max_ = 0

        """
        index: 0 1 2 3 4 5 6 7
        v     [0,2,1,5,6,2,3,0]
        stack: 
        index  0 2 3 4 
        height 0 1 5 6 
        """
        for i, next_value in enumerate(heights):  # 0, 0 # 2, 1 # 3, 5 # 5, 2
            while mono_inc_stack and heights[mono_inc_stack[-1]] > next_value:
                poped_index = mono_inc_stack.pop()  # 4
                poped_value = heights[poped_index]  # 6
                length = i if not mono_inc_stack else i - mono_inc_stack[-1] - 1  # 2 - 0 - 1
                max_ = max(max_, poped_value * length)

            mono_inc_stack.append(i)

        return max_  # 2
