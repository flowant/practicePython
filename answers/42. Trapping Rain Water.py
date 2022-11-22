class Solution:
    def trap(self, height: List[int]) -> int:
        """
        42. Trapping Rain Water
        https://leetcode.com/problems/trapping-rain-water/description/

        indices   0 1 2 3 4 5 6 7 8 9 10 11
        height = [0,1,0,2,1,0,1,3,2,1 ,2 ,1]

        max_heights = [
            (1, 1),
            (3, 2),
            (7, 3),
            (10, 2),
            (11, 1),
        ]

        max_heights_from_right_to_left = [
            (11, 1),
            (10, 2),
            (7, 3),
        ]

        boundary_map = {
           2: 1,   1
           4: 2,   1
           5: 2,   2
           6: 2,   1
           8: 2,   0
           9: 2,   1
        }

        """

        if not height:
            return 0

        max_heights = []
        max_indices = set()
        max = 0
        for i, h in enumerate(height):
            if h > max:
                max = h
                max_heights.append((i, h))
                max_indices.add(i)

        max_heights_from_right_to_left = []
        max = 0
        for i, h in reversed(list(enumerate(height))):
            if h > max:
                max = h
                max_heights_from_right_to_left.append((i, h))

        while max_heights_from_right_to_left:
            i, h = max_heights_from_right_to_left.pop()
            if i not in max_indices:
                max_heights.append((i, h))

        # At least two boundaries are required
        if len(max_heights) < 2:
            return 0

        prev_index, prev_height = max_heights[0]  # (1, 1) (3, 2)

        boundary_map = dict()

        for cur_index, cur_height in max_heights[1:]:  # (3, 2), (7, 3),
            min_height = min(prev_height, cur_height)  # 1, 2
            for i in range(prev_index + 1, cur_index):
                boundary_map[i] = min_height
            prev_index = cur_index  #
            prev_height = cur_height

        sum = 0
        for i, h in enumerate(height):
            if i in boundary_map:
                sum += boundary_map[i] - h

        return sum


