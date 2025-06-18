from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the initial prefix
        prefix = strs[0]
        
        for s in strs[1:]:
            # Reduce the prefix until it matches the beginning of the current string
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
