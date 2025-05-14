class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        
        while columnNumber > 0:
            columnNumber -= 1  # Adjust to 0-indexed (Excel columns are 1-indexed)
            result.append(chr(columnNumber % 26 + ord('A')))  # Find corresponding letter
            columnNumber //= 26  # Move to the next digit in the base-26 system
        
        return ''.join(result[::-1])  # Reverse the result to get the correct column title

