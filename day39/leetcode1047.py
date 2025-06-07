class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()  # remove the previous one because it's a duplicate
            else:
                stack.append(char)
        return ''.join(stack)
