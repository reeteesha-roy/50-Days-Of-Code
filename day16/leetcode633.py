import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a * a <= c:
            b_squared = c - a * a
            b = int(math.sqrt(b_squared))
            if b * b == b_squared:
                return True
            a += 1
        return False
