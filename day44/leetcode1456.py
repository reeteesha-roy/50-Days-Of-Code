class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vowels = current_vowels = 0
        
        # Initialize the first window
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        max_vowels = current_vowels
        
        # Slide the window through the rest of the string
        for i in range(k, len(s)):
            # Remove the leftmost character of the previous window
            if s[i - k] in vowels:
                current_vowels -= 1
            # Add the new character
            if s[i] in vowels:
                current_vowels += 1
            # Update the maximum
            if current_vowels > max_vowels:
                max_vowels = current_vowels
                # Early exit if we find the maximum possible
                if max_vowels == k:
                    return max_vowels
        
        return max_vowels
