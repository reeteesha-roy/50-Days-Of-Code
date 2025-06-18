# 🚀 Day 47 – #DrGViswanathan 50 Days Coding Challenge

Today's problems focused on substring counting techniques and bit manipulation fundamentals, demonstrating efficient string analysis and binary representation operations.

---

## 💫 String Challenge: Number of Substrings with Only 1s (LeetCode 1358)

**Problem:**  
Given a binary string `s`, return the number of substrings that contain only 1s. Since the answer may be large, return it modulo 10^9 + 7.

**Approach:**  
Use mathematical counting with consecutive segments:
1. Iterate through the string and identify consecutive segments of 1s.
2. For a segment of length `k`, the number of substrings containing only 1s is `k * (k + 1) / 2`.
3. This formula counts all possible substrings within the segment: single chars, pairs, triplets, etc.
4. Sum up contributions from all segments and apply modulo operation.

**Time Complexity:** O(n), where n is the length of the string  
**Space Complexity:** O(1)

**Why this works:**  
For a consecutive sequence of `k` ones, we can form substrings of lengths 1, 2, ..., k. The total count follows the arithmetic series formula. By identifying segments and applying this formula, we avoid the O(n²) brute force approach.

---

## 💫 Bit Manipulation Challenge: Number of 1 Bits / Hamming Weight (LeetCode 191)

**Problem:**  
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

**Approach:**  
Use efficient bit manipulation techniques:
1. **Method 1 - Bit by Bit:** Check each bit using `n & 1`, then right shift `n >>= 1`.
2. **Method 2 - Brian Kernighan's Algorithm:** Use `n & (n-1)` to remove the rightmost set bit in each iteration.
3. **Method 3 - Built-in:** Use `bin(n).count('1')` for simplicity.

**Time Complexity:** O(log n) for Method 1, O(number of set bits) for Method 2  
**Space Complexity:** O(1)

**Why this works:**  
Brian Kernighan's algorithm is optimal because `n & (n-1)` cleverly removes the rightmost 1-bit. This means we only iterate as many times as there are 1-bits, making it faster than checking every bit position.

---

## 💡 Key Takeaways:
- Mathematical formulas can dramatically optimize substring counting problems by avoiding nested loops.
- Bit manipulation algorithms like Brian Kernighan's technique provide elegant solutions that work directly with binary representations.
