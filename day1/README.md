# 🚀 Day 1 – #DrGViswanathan 50 Days Coding Challenge

As part of the #DrGViswanathan 50 Days Coding Challenge, I’ll be tackling one DSA and one math-based problem daily, sharing not just the solutions but the approach and takeaways behind them.

---

## 💫 DSA Challenge: Reverse Linked List (LeetCode 206)
**Problem:** Reverse a singly linked list.

### Approach:
Used an iterative method with three pointers: `prev`, `curr`, and `next`. Traversed the list while reassigning each node’s `next` to point backward. Once the loop completes, `prev` points to the new head of the reversed list.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)  
- **Why this works:** Efficient pointer manipulation ensures in-place reversal without auxiliary data structures.

---

## 💫 Math-based Challenge: Missing Number (LeetCode 268)
**Problem:** Given an array with numbers from 0 to n (one missing), identify the missing number.

### Approach:
Calculated the expected sum using the formula `n * (n + 1) / 2` and compared it to the actual sum of the array elements. The difference reveals the missing value.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)  
- **Why this works:** Leverages basic arithmetic to sidestep iteration-heavy logic.

---

## 💡 Key Takeaways:
- **Linked Lists:** Success lies in pointer precision — it's about control and clarity at every step.
- **Math Problems:** When the problem is numerical, pattern recognition often outpaces brute-force solutions. Understanding fundamentals pays off.
