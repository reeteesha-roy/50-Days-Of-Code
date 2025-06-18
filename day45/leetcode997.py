from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Initialize two arrays to count trust relationships
        trust_given = [0] * (n + 1)  # How many people this person trusts
        trust_received = [0] * (n + 1)  # How many people trust this person
        
        for a, b in trust:
            trust_given[a] += 1
            trust_received[b] += 1
        
        # Check each person to see if they meet the judge criteria
        for i in range(1, n + 1):
            if trust_given[i] == 0 and trust_received[i] == n - 1:
                return i
        
        return -1
