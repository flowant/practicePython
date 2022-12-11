class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        1209. Remove All Adjacent Duplicates in String II

        Input: s = "deeedbbcccbdaa", k = 3


        use stack
           - counter [1]
           - string  [d

           # corner case: stack is empty
           when stack[-1] != letter, push the letter and 1 to the counter stack
           when stack[-1] == letter and counter[-1] == k -1, pop k - 2 element from letter stack, and pop 1 element from the counter stack
           and counter(index -1) == 2
        Time and Space complexity: O(n)
        """
        if not s or k is None:
            return ""

        stack_letter = []  # d d b
        stack_counter = []  # 2 1

        # Input: s = "deeedbbcccbdaa", k = 3

        for letter in s:  # e
            if not stack_letter or letter != stack_letter[-1]:
                stack_letter.append(letter)
                stack_counter.append(1)
            elif letter == stack_letter[-1]:
                if stack_counter[-1] == k - 1:
                    stack_counter.pop()
                    while stack_letter and letter == stack_letter[-1]:
                        stack_letter.pop()
                else:
                    stack_counter[-1] += 1
                    stack_letter.append(letter)

        return "".join(stack_letter)
