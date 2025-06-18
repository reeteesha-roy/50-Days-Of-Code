class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        
        if n == 1:
            return ""
        
        chars = list(palindrome)
        
        for i in range(n // 2):
            if chars[i] != 'a':
                chars[i] = 'a'
                return ''.join(chars)
        
        chars[n - 1] = 'b'
        return ''.join(chars)
