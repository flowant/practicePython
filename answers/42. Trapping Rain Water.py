class Solution:
    def trap(self, height: List[int]) -> int:
        """
        42. Trapping Rain Water


        decreasing mono stack
        - when height is bigger than top of the stack pop.

        i 0 1 2 3 4 5 6 7 8 9 0 1
        v[0,1,0,2,1,0,1,3,2,1,2,1]

                        |
                | W W W | | W |
            | W | | W | | | | | |

        monotonic decreasing stack
        i[7 8 10 11]
        v[3 2 2 1]

        987654321

        (right wall)
        current_index = 10
        current_value = 2

        (bottom)
        poped_i = 9
        poped_v = 1

        # if stack is empty, exit inner loop
        (left wall)
        top_i = 8
        top_v = 2

        distance = current_index - top_i - 1  # 10 - 8 - 1 = 1
        height = min(top_v, current_value) - poped_v  # 2 - 1 = 1

        water_volumn += height * distance  # 1 + 1 + 0 + 3 + 1
        """

        if not height:
            return 0
        if len(height) < 2:
            return 0

        water_volumn = 0
        mono_desc_stack = []  #

        """
        i 0 1 2 3 4 5 6 7 8 9 0 1
        v[0,1,0,2,1,0,1,3,2,1,2,1]

                        | 
                | W W W | | W |
            | W | | W | | | | | |

        mono_desc_stack = [0]
        """

        for i, current_wall_height in enumerate(height):  # 1, 1

            while (mono_desc_stack and height[mono_desc_stack[-1]] < current_wall_height):
                bottom_height = height[mono_desc_stack[-1]]
                mono_desc_stack.pop()

                if not mono_desc_stack:
                    break

                left_wall_index = mono_desc_stack[-1]
                left_wall_height = height[left_wall_index]

                distance = i - left_wall_index - 1
                wall_height = min(left_wall_height, current_wall_height) - bottom_height

                water_volumn += distance * wall_height

            mono_desc_stack.append(i)

        return water_volumn
