# 🚀 Day 49 – #DrGViswanathan 50 Days Coding Challenge

Today's problems combined number theory fundamentals with bit manipulation techniques, showcasing prime number generation algorithms and XOR properties for finding unique elements in arrays.

---

## 💫 Number Theory Challenge: Count Primes (LeetCode 204)

**Problem:**  
Given an integer `n`, return the number of prime numbers that are strictly less than `n`.

**Approach:**  
Use the Sieve of Eratosthenes algorithm:
1. Create a boolean array `is_prime` of size `n`, initially all `True`.
2. Mark 0 and 1 as non-prime (if they exist in range).
3. For each number `i` from 2 to √n:
   - If `i` is still marked as prime, mark all its multiples starting from `i²` as non-prime.
   - Start from `i²` because smaller multiples would have been marked by smaller primes.
4. Count remaining `True` values in the array.

**Time Complexity:** O(n log log n)  
**Space Complexity:** O(n)

**Why this works:**  
The Sieve of Eratosthenes efficiently eliminates composite numbers by marking multiples of each prime. Starting from `i²` avoids redundant work, and only checking up to √n is sufficient because any composite number larger than √n would have already been marked by its smaller prime factors.

---

## 💫 Bit Manipulation Challenge: Single Number (LeetCode 136)

**Problem:**  
Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one. You must implement a solution with linear runtime complexity and use only constant extra space.

**Approach:**  
Use XOR operation properties:
1. Initialize `result = 0`.
2. XOR all elements in the array: `result ^= num` for each num.
3. Return the final result.
4. **Key Properties of XOR:**
   - `a ^ a = 0` (any number XORed with itself is 0)
   - `a ^ 0 = a` (any number XORed with 0 is itself)
   - XOR is commutative and associative

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

**Why this works:**  
Since every element appears twice except one, XORing all elements will cancel out the pairs (each pair XORs to 0), leaving only the single element. The mathematical property `a ^ a = 0` makes duplicate elements disappear, while `a ^ 0 = a` preserves the unique element.

---

## 💡 Key Takeaways:
- The Sieve of Eratosthenes remains one of the most efficient algorithms for generating multiple primes through systematic elimination.
- XOR operations provide elegant solutions for problems involving pairs and uniqueness due to their self-canceling properties.
