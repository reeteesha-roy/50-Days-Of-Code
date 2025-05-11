# 🚀 Day 11 – #DrGViswanathan 50 Days Coding Challenge

Staying sharp with a number theory dive and list manipulation finesse. Let’s go! 💥

---

## 💫 DSA Challenge: Remove Nth Node From End of List (LeetCode 19)
**Problem:** Given the head of a singly linked list, remove the nth node from the end of the list and return its head.

### Approach:
1. **Dummy Node:** Simplifies edge cases, such as removing the head node.
2. **Two-pointer technique:** 
   - First, move the fast pointer `n+1` steps ahead.
   - Then, move both pointers (fast and slow) until the fast pointer reaches the end.
3. **Remove the Node:** After the loop, the slow pointer will be just before the node to be removed. Update the `next` pointer of the slow pointer to skip the target node.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)  
- **Why this works:** This approach ensures a single traversal of the list, making it optimal for this problem.

---

## 💫 Math-based Challenge: Factorial Trailing Zeroes (LeetCode 172)
**Problem:** Given an integer `n`, return the number of trailing zeroes in `n!`.

### Approach:
1. **Trailing Zeroes Insight:** Trailing zeroes are produced by factors of `10`. Since `10 = 2 × 5`, and there are always more factors of `2` than factors of `5`, the problem reduces to counting how many times `5` is a factor in the numbers from `1` to `n`.
2. **Solution:** Repeatedly divide `n` by powers of `5` (i.e., `5, 25, 125...`) until `n` is less than 5.

- **Time Complexity:** O(log n)  
- **Space Complexity:** O(1)  
- **Why this works:** By counting multiples of `5`, we capture all the trailing zeroes created by factors of `5`.

---

## 💡 Key Takeaways:
- **Linked Lists:** Two-pointer techniques can efficiently solve problems that would otherwise require multiple passes.
- **Math Problems:** Understanding the underlying factors (in this case, multiples of 5) gives a clean, optimized solution without unnecessary calculations.
