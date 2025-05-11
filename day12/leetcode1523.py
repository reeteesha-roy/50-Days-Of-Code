class Solution:
    def countOdds(self, low: int, high: int) -> int:
         # Calculate the count by determining how many odd numbers are in the range
        # If low is odd, then the first number in the range is odd
        # If high is odd, then the last number in the range is odd
        return (high + 1) // 2 - low // 2
