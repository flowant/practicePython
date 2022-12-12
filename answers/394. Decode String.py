class Solution:
    def decodeString(self, s: str) -> str:
        """
        394. Decode String

        Input: s = "3[a2[c]]"
        Input: s = "2[abc]3[cd]ef"

        stack_digit (), int("".join(digit))
        stack_substring ()

        digit_list []
        sub_string_list [a b c a b c c d c d c d e f]

        rule:
        - when c is [ then push to stack, digit = "", sub_string ""
        - when c is ] then substring = substring[-1] + substring * digit[-1]
          pop two stacks

        #corner case: check stack is empty

        restun "".join(sub_string_list)

        Time complexity: O(max_string_in_bracket * digit * n / 3)
        input = 4[a[3[b[2[c]]]]]  n = 15, ] n/3
        Space complexity: product of digits of max nexted bracket
        """
        if not s:
            return ""

        stack_digit = []
        stack_substring = []

        digit_list = list()
        substring_list = list()

        for c in s:  # 3 [ a
            if c == '[':
                stack_digit.append(int("".join(digit_list)))  # 3
                digit_list = []
                stack_substring.append(substring_list)  # []
                substring_list = []
            elif c == ']':
                substring_list = stack_substring[-1] + (
                            substring_list * stack_digit[-1])  # [a c c], [] + [a c c] * = [ a c c a c c a c c]
                stack_substring.pop()
                stack_digit.pop()
            elif c.isdigit():
                digit_list.append(c)  #
            else:  # letter
                substring_list.append(c)  # c

        return "".join(substring_list)
