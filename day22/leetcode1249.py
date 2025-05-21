class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_list = list(s)
        stack = []

        # Mark parentheses to remove
        for i, char in enumerate(s_list):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s_list[i] = ''  # Mark for removal

        # Remove unmatched '(' left in stack
        for i in stack:
            s_list[i] = ''

        return ''.join(s_list)

        
