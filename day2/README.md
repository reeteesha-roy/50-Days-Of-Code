# 🚀 Day 2 – #DrGViswanathan 50 Days Coding Challenge

Continuing the challenge with a balanced mix of pointer precision and mathematical insight.

---

## 💫 DSA Challenge: Middle of the Linked List (LeetCode 876)
**Problem:** Given a singly linked list, return the middle node. If there are two middles, return the second one.

### Approach:
Used the **two-pointer** technique: 
- A `slow` pointer moves one node at a time.
- A `fast` pointer moves two nodes at a time.
When `fast` reaches the end, `slow` is positioned at the middle.

The method handles edge cases (empty or single-node lists) and efficiently finds the middle of the list in one pass.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)  
- **Why this works:** Efficiently identifies the midpoint in a single traversal without counting nodes.

---

## 💫 Math-based Challenge: Add Digits (LeetCode 258)
**Problem:** Given a number `num`, repeatedly add its digits until the result is a single digit.

### Approach:
Used the **Digital Root** concept from number theory:
- For any non-zero number, the result is `1 + ((num - 1) % 9)`.

This formula gives the answer in constant time without loops or recursion.

- **Time Complexity:** O(1)  
- **Space Complexity:** O(1)  
- **Why this works:** Mathematical properties of base-10 ensure the result cycles in a predictable pattern.

---

## 💡 Key Takeaways:
- **Linked List Tricks:** Two-pointer patterns are versatile and powerful for problems involving positions or lengths.
- **Math Optimization:** Recognizing known number theory patterns can turn a multi-step process into a one-liner.

