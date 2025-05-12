class Solution:
    def arraySign(self, nums: list[int]) -> int:
        sign = 1  # start assuming the product is positive

        for num in nums:
            if num == 0:
                return 0  # product will definitely be zero
            elif num < 0:
                sign *= -1  # flip the sign

        return sign

