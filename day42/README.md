# 🚀 Day 42 – #DrGViswanathan 50 Days Coding Challenge

Today's problems explored array manipulation with two-pointer techniques and bit manipulation fundamentals, showcasing efficient algorithms for sum problems and binary operations.

---

## 💫 Array Challenge: 3Sum (LeetCode 15)

**Problem:**  
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. The solution set must not contain duplicate triplets.

**Approach:**  
Use sorting combined with two-pointer technique:
1. Sort the array to enable two-pointer approach and easy duplicate handling.
2. For each element as the first number, use two pointers to find pairs that sum to the negative of that number.
3. Skip duplicates by moving pointers past identical values.
4. If sum is too small, move left pointer right; if too large, move right pointer left.

**Time Complexity:** O(n²)  
**Space Complexity:** O(1) excluding output space

**Why this works:**  
Sorting enables efficient duplicate elimination and two-pointer technique. By fixing one element and finding pairs for the remaining sum, we reduce the problem from O(n³) brute force to O(n²).

---

## 💫 Bit Manipulation Challenge: Number of 1 Bits (LeetCode 191)

**Problem:**  
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

**Approach:**  
Use bit manipulation to count set bits:
1. Initialize a counter to 0.
2. While the number is not zero, check if the least significant bit is 1.
3. Right shift the number to examine the next bit.
4. Continue until all bits are processed.

**Alternative Optimization:** Use `n & (n-1)` trick that removes the rightmost set bit in each iteration.

**Time Complexity:** O(log n) or O(number of set bits)  
**Space Complexity:** O(1)

**Why this works:**  
Bitwise operations directly manipulate the binary representation. The `n & 1` operation isolates the least significant bit, and right shifting systematically examines each bit position.

---

## 💡 Key Takeaways:
- Two-pointer technique combined with sorting is powerful for sum-based problems and duplicate elimination.
- Bit manipulation provides efficient solutions for binary operations, often with constant space complexity.
