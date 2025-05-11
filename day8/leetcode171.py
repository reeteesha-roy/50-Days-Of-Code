class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
    
        result = 0
        
        # Iterate through each character in the column title
        for char in columnTitle:
    
            result = result * 26
            result += ord(char) - ord('A') + 1
            
        return result
