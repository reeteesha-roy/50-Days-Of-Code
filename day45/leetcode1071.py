class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenated strings are equal in both orders
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the GCD of the lengths
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]
