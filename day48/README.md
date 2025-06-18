# 🚀 Day 48 – #DrGViswanathan 50 Days Coding Challenge

Today's problems explored mathematical sequence validation and bit manipulation distance calculations, demonstrating arithmetic progression properties and XOR-based bit difference analysis.

---

## 💫 Array Challenge: Can Make Arithmetic Progression From Sequence (LeetCode 1250)

**Problem:**  
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same. Given an array of numbers `arr`, return `true` if the array can be rearranged to form an arithmetic progression, otherwise return `false`.

**Approach:**  
Use sorting and mathematical validation:
1. **Method 1 - Sorting Approach:** Sort the array and check if consecutive differences are equal.
2. **Method 2 - Set-based Approach:** Calculate expected common difference, then verify all expected values exist.
3. Find minimum and maximum values, calculate common difference as `(max - min) / (n - 1)`.
4. Check if the difference is an integer and all arithmetic sequence values are present.

**Time Complexity:** O(n log n) for sorting approach, O(n) for set approach  
**Space Complexity:** O(1) for sorting, O(n) for set approach

**Why this works:**  
In an arithmetic progression, the common difference is fixed. By sorting or using the mathematical property that `difference = (max - min) / (n - 1)`, we can efficiently validate if the array can form such a sequence.

---

## 💫 Bit Manipulation Challenge: Hamming Distance (LeetCode 461)

**Problem:**  
The Hamming distance between two integers is the number of positions at which the corresponding bits are different. Given two integers `x` and `y`, return the Hamming distance between them.

**Approach:**  
Use XOR operation with bit counting:
1. **Step 1:** Compute `xor_result = x ^ y`. XOR gives 1 where bits differ, 0 where they're same.
2. **Step 2:** Count the number of 1-bits in the XOR result.
3. **Method 1:** Use bit-by-bit checking with `& 1` and right shift.
4. **Method 2:** Use Brian Kernighan's algorithm with `n & (n-1)` to count set bits efficiently.
5. **Method 3:** Use built-in `bin(xor_result).count('1')`.

**Time Complexity:** O(log n), where n is the larger of x and y  
**Space Complexity:** O(1)

**Why this works:**  
XOR is perfect for finding bit differences because it outputs 1 only when input bits differ. Counting the 1-bits in the XOR result directly gives us the Hamming distance, representing positions where the original numbers had different bits.

---

## 💡 Key Takeaways:
- Arithmetic progressions have predictable mathematical properties that can be validated without full enumeration.
- XOR operation combined with bit counting provides an elegant solution for measuring binary differences between numbers.
