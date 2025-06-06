import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Use regex to keep only alphanumeric characters and convert to lowercase
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # Check if the cleaned string is equal to its reverse
        return cleaned == cleaned[::-1]
