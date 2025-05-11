class Solution:
    def bulbSwitch(self, n: int) -> int:
        
        def brute_force(n):
            # Initialize all bulbs to off (False means off, True means on)
            bulbs = [False] * n
            
            # First round: turn on all bulbs
            for i in range(n):
                bulbs[i] = True
                
            # For each round from 2 to n
            for round in range(2, n + 1):
                # Toggle every round-th bulb
                for i in range(round - 1, n, round):
                    bulbs[i] = not bulbs[i]
            
            # Count how many bulbs are on
            return sum(bulbs)
        
        return int(n ** 0.5)
