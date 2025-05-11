# 🚀 Day 9 – #DrGViswanathan 50 Days Coding Challenge

Today’s grind: pointer gymnastics to swap list values, and digit hunting without building giant numbers. 🔍📈

---

## 💫 DSA Challenge: Swap Nodes in a Linked List (LeetCode 1721)
**Problem:** Swap the values of the kth node from the beginning and the kth node from the end in a singly linked list.

### Approach:
Two possible approaches:
1. **Two-pass method:**  
   - First loop to find the length.
   - Then identify the `k`th node from the start and the `k`th from the end (at position `length - k + 1`).
2. **Optimized one-pass method (used):**  
   - Move a pointer `k` steps to get the front node.
   - Then run a second pointer in parallel with the front node until it reaches the end. This lands the second pointer at the `k`th node from the end.
   - Swap their values.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)  
- **Why this works:** You're not re-linking nodes — just swapping values. Makes it faster and safer.

---

## 💫 Math-based Challenge: Nth Digit (LeetCode 400)
**Problem:** Find the nth digit in the infinite sequence `123456789101112...`.

### Approach:
1. Identify how many digits the `n`th digit belongs to:
   - 1-digit numbers: 1–9 (9 total)
   - 2-digit numbers: 10–99 (90 total, each with 2 digits)
   - 3-digit numbers: 100–999 (900 total, each with 3 digits)
2. Narrow down which number contains the `n`th digit.
3. Convert that number to a string and return the correct digit.

- **Time Complexity:** O(log n) due to narrowing down by digit groups  
- **Space Complexity:** O(1)  
- **Why this works:** You don’t need to construct the whole sequence — just do the math and zoom straight into the target number.

---

## 💡 Key Takeaways:
- **Linked Lists:** One-pass pointer techniques can replace length-based logic when memory is tight and time matters.
- **Math Problems:** Digit manipulation problems are often about patterns, not brute force.


