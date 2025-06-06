import math

class Solution:
    def replaceNonCoprimes(self, nums):
        stack = []

        for num in nums:
            # Try to merge with the top of the stack if possible
            while stack:
                gcd_val = math.gcd(stack[-1], num)
                if gcd_val == 1:
                    break  # Coprime, no merge
                # Non-coprime: replace with LCM
                num = (stack[-1] * num) // gcd_val
                stack.pop()
            stack.append(num)

        return stack

