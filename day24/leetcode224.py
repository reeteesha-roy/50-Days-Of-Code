class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        result = 0
        sign = 1  # 1 means +, -1 means -

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in "+-":
                result += sign * num
                num = 0
                sign = 1 if char == '+' else -1
            elif char == '(':
                # Push current result and sign onto the stack
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += sign * num
                num = 0
                result *= stack.pop()  # sign before parenthesis
                result += stack.pop()  # result before parenthesis

        return result + (sign * num)
