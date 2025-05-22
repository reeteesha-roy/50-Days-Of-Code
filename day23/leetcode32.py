class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize stack with -1 to handle base case
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push the index of '('
            else:
                stack.pop()  # Pop the last unmatched '('
                if not stack:
                    stack.append(i)  # No unmatched '(', push current index as base
                else:
                    max_len = max(max_len, i - stack[-1])  # Valid substring length

        return max_len
