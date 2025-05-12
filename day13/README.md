# 🚀 Day 13 – #DrGViswanathan 50 Days Coding Challenge

Today we are working with removing duplicates from sorted lists and sign of product of an array. Let's dive in!

---

## 💫 DSA Challenge: Remove Duplicates from Sorted List II (LeetCode 82)

**Problem:** Given the head of a **sorted** linked list, delete all nodes that have duplicate numbers, leaving **only distinct numbers** from the original list.

### Approach:
1. **Dummy Node Trick:** Start with a dummy node pointing to the head to handle edge cases smoothly.
2. **Two-Pointer Game:** Use `prev` to track the last node before a duplicate sequence and `current` to iterate through the list.
3. **Skip the Duplicates:** If you detect a duplicate streak (`current.val == current.next.val`), keep moving `current` until the value changes, then link `prev.next` to the non-duplicate node.
4. **Keep It Moving:** Otherwise, move both pointers forward.

- **Time Complexity:** O(n), where `n` is the number of nodes in the list.  
- **Space Complexity:** O(1) – in-place list manipulation.  
- **Why this works:** Since the list is sorted, duplicates are grouped together. We can detect and remove them in one pass.

---

## 💫 Math-based Challenge: Sign of the Product of an Array (LeetCode 1822)

**Problem:** You’re given an array `nums`. Return:
- `1` if the product of all elements is positive,
- `-1` if it’s negative,
- `0` if **any** element is `0`.

### Approach:
1. **Avoid Full Product:** Don’t compute the full product (that’s a trap!). Instead, just track the **sign**.
2. **Initialize `sign = 1`:** Assume positive to start.
3. **Flip on Negatives:** Every negative number flips the sign: `sign *= -1`.
4. **Zero is King:** If you hit a `0`, return `0` immediately.

- **Time Complexity:** O(n), one pass through the array.  
- **Space Complexity:** O(1), no extra storage needed.  
- **Why this works:** The sign of a product only depends on the number of negative values and whether zero exists — no multiplication required!

---

## 💡 Key Takeaways:
- **Linked Lists:** Sometimes solving the problem cleanly means using a dummy node. Don’t sleep on that move — it's a classic for a reason.
- **Math Problems:** Understanding the **nature of the problem** (signs, zeros, etc.) lets you **optimize** the solution without going through unnecessary steps. No need to calculate full products when you can work with just signs!

