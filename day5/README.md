# 🚀 Day 5 – #DrGViswanathan 50 Days Coding Challenge

Palindrome detection, but make it *linked list edition*. And a binary search flex on perfect squares.

---

## 💫 DSA Challenge: Palindrome Linked List (LeetCode 234)
**Problem:** Check if a singly linked list is a palindrome.

### Approach:
Used a **three-step strategy**:
1. **Find the middle** of the list using the slow/fast pointer technique.
2. **Reverse the second half** of the list in-place.
3. **Compare** the first half and the reversed second half node by node.

Only compared half the list to optimize performance. Reversal is done without extra space.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)  
- **Why this works:** Efficient and in-place, this method avoids using extra memory (like stacks or list copies) while maintaining clean symmetry checking.

---

## 💫 Math-based Challenge: Valid Perfect Square (LeetCode 367)
**Problem:** Determine if a given positive integer is a perfect square.

### Approach:
Used a **binary search** between `2` and `num // 2`:
- Calculated the square of `mid` in each iteration.
- If `mid² == num`, it’s a perfect square.
- Otherwise, narrowed the range accordingly.

Early exit for small numbers like 1.

- **Time Complexity:** O(log n)  
- **Space Complexity:** O(1)  
- **Why this works:** Binary search significantly cuts down the number of checks compared to linear iteration — efficient for large inputs.

---

## 💡 Key Takeaways:
- **Linked Lists:** Reversing in-place and comparing half-slices is a solid trick for space-efficient palindrome checks.
- **Math Problems:** Binary search isn’t just for arrays — it shines in numeric problems with sorted-like logic too.
