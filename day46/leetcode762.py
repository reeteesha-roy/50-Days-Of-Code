class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Predefined set of primes up to 32 (since 10^6 has max 20 bits)
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        count = 0
        
        for num in range(left, right + 1):
            set_bits = bin(num).count('1')
            if set_bits in primes:
                count += 1
        
        return count
