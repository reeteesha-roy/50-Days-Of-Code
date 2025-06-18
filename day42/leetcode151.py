class Solution:
    def reverseWords(self, s: str) -> str:
        # Trim leading and trailing spaces
        s = s.strip()
        
        words = []
        current_word = []
        
        for char in s:
            if char != ' ':
                current_word.append(char)
            elif current_word:
                words.append(''.join(current_word))
                current_word = []
        
        if current_word:
            words.append(''.join(current_word))
        
        return ' '.join(reversed(words))
