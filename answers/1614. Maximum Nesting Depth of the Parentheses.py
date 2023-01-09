class Solution:
    def maxDepth(self, s: str) -> int:
        """
        1614. Maximum Nesting Depth of the Parentheses

        Input: s = "(1+(2*3)+((8)/4))+1"
        Output: 3


        using stack, append '(' character into the stack, pop the top from the stack when the character is ')'
        max_depth = max(max_depth, len(stack))

        Time Complexity: O(n), n is the length of the input string
        Space Complexity: O(n/2)
        Space Complexity: O(1), we can keep only the size of stack because stack contains only '(' character

        """

        # input validation
        if not s:
            return 0

        max_depth = 0
        stack_size = 0  # 0
        # stack = list()

        # input s: "(1+(2*3)+((8)/4))+1"
        for c in s:
            if c == '(':
                stack_size += 1
                # stack.append(c)
                max_depth = max(max_depth, stack_size)  # 3
                # max_depth = max(max_depth, len(stack))
            if c == ')':
                stack_size -= 1
                # stack.pop()

        return max_depth
