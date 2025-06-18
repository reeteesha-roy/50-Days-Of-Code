class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        
        # Find GCD of all elements in the array
        result_gcd = nums[0]
        for i in range(1, len(nums)):
            result_gcd = math.gcd(result_gcd, nums[i])
            # Optimization: if GCD becomes 1, we can return early
            if result_gcd == 1:
                return True
        
        return result_gcd == 1
