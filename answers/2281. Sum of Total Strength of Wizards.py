class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        """
        2281. Sum of Total Strength of Wizards
        Input: strength = [3  5  1  4]

        For each element, find all sub arrays which contains the element as the minimum.
        Over input strength,
          result += sum of sub arrays * element

        ps = prefix sum, aps = accumulative prefix sum
        i   0  1  2  3  4  5
        ps  0  3  8  9  13 13         aps(3) = ps(0) + ps(1) + ps(2) + ps(3)
        aps 0  3  11 20 33 52         aps(3) - aps(1) = ps(3) + ps(2) = 17

          i 0  1  2  3  | 4
          v 3  5  1  4  | 0

            L     m  R

        i 0 to 2  -ps[L](0)  +ps[m+1](9)    = 9
        i 0 to 3  -ps[L](0)  +ps[R+1](13)   = 13
        i 1 to 2  -ps[L+1](3) +ps[m+1](9)   = 6
        i 1 to 3  -ps[L+1](3) +ps[R+1](13)  = 10
        i 2 to 2  -ps[m](8)   +ps[m+1](9)   = 1
        i 2 to 3  -ps[m](8)   +ps[R+1](13)  = 5
                                            = 44
        - 2(ps[L] + ps[L+1] + ps[m]) + 3*(ps[m+1] + ps[R+1])
                -2(0 + 3 + 8) = -22  +         3*( 9  13 = 22) = 66  =44
        - (R - m + 1)(aps[m] - aps[max(L-1, 0)]) + (m - L + 1)(aps[R+1]-aps[m])
        - (3 - 2 + 1)(11 - 0)                    + (2 - 0 + 1)(33 - 11 )

        i 0  1  2  3  | 4
        v 3  5  1  4  | 0

        iteration i: 4
                  v: 0
        monotonic increasing stack
        index
        value

        L = top + 1 = 1 0 3 0
        (L is 0 when stack is empty)
        popped i      1 0 3 2
        R = i - 1   = 1 1 3 3
        popped v      5 3 4 1
        min*sum of sub array
                      5*5
                      11*3
                      4*4
                      44*1
        result +=

        Time, Space Complexity: O(n)
        """

        if not strength:
            return 0

        MOD = 10 ** 9 + 7
        result = 0
        prefix_sum = 0
        acc_prefix_sum = [0]
        mono_inc_stack = []

        strength.append(0)

        for i, next_value in enumerate(strength):
            right_index = i - 1
            prefix_sum += next_value
            acc_prefix_sum.append(acc_prefix_sum[-1] + prefix_sum)

            while mono_inc_stack and strength[mono_inc_stack[-1]] > next_value:
                min_index = mono_inc_stack.pop()
                min_value = strength[min_index]
                left_index = 0 if not mono_inc_stack else mono_inc_stack[-1] + 1

                len_right = right_index - min_index + 1
                left = acc_prefix_sum[min_index] - acc_prefix_sum[max(left_index - 1, 0)]
                len_left = min_index - left_index + 1
                right = acc_prefix_sum[right_index + 1] - acc_prefix_sum[min_index]
                # - (R - m + 1)(sps[m] - sps[max(L-1, 0)]) + (m - L + 1)(sps[R+1] - sps[m])

                result += min_value * (len_left * right - len_right * left)

            mono_inc_stack.append(i)

        return result % MOD
