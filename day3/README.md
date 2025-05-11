# 🚀 Day 3 – #DrGViswanathan 50 Days Coding Challenge

Focused on mastering classic linked list merging and diving into number theory with perfect numbers.

---

## 💫 DSA Challenge: Merge Two Sorted Lists (LeetCode 21)
**Problem:** Merge two sorted linked lists and return the head of the new sorted list.

### Approach:
Used a **dummy node** to simplify edge case handling and a pointer (`current`) to build the merged list iteratively. Compared nodes from both lists and attached the smaller one to the merged list. Once one list is exhausted, attached the remaining part of the other list.

This approach handles:
- All combinations of input list lengths
- Clean merging without recursion

- **Time Complexity:** O(n + m), where n and m are the lengths of the input lists  
- **Space Complexity:** O(1)  
- **Why this works:** Maintains constant space and avoids unnecessary object creation by reusing original nodes.

---

## 💫 Math-based Challenge: Perfect Number (LeetCode 507)
**Problem:** Check if a given number is a **perfect number** — i.e., equal to the sum of its proper divisors (excluding itself).

### Approach:
Started with a base check (`num <= 1` is automatically false). Initialized the sum of divisors to 1 (since 1 is a proper divisor of every number). Then, looped from 2 to √num:
- For every divisor `i`, added both `i` and `num // i` to the sum (if distinct).
- Finally, compared the sum to the original number.

- **Time Complexity:** O(√n)  
- **Space Complexity:** O(1)  
- **Why this works:** Only checks up to the square root and avoids redundant divisor calculations for efficiency.

---

## 💡 Key Takeaways:
- **Linked Lists:** Dummy nodes are a powerful pattern to simplify list construction and edge case management.
- **Math Problems:** Divisor-based logic benefits from symmetry — if `i` divides `n`, so does `n // i`. Efficient looping pays off.

