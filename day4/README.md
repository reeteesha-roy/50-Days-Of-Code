# 🚀 Day 4 – #DrGViswanathan 50 Days Coding Challenge

Today’s theme: cycle detection with speed differentials and number theory with digit reversal. 🔁🔢

---

## 💫 DSA Challenge: Linked List Cycle (LeetCode 141)
**Problem:** Determine if a linked list has a cycle in it.

### Approach:
Applied the classic **Floyd’s Cycle Detection Algorithm** (aka "Tortoise and Hare"):
- Used two pointers — `slow` moves one step, `fast` moves two.
- If there’s a cycle, they’ll eventually meet inside the loop.
- If `fast` reaches the end (`None`), then there’s no cycle.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)  
- **Why this works:** Differing speeds mean that, in a cycle, the faster pointer will lap the slower one — like two runners on a track.

---

## 💫 Math-based Challenge: Palindrome Number (LeetCode 9)
**Problem:** Check if a non-negative integer is a palindrome (reads the same backward and forward).

### Approach:
Instead of reversing the whole number (which could lead to overflow or inefficiency), only reversed **half** of it:
- If `x < 0` or ends with 0 but isn’t 0, it’s not a palindrome.
- Built a reversed number from the last digits of `x` until the original number shrunk below or equal to it.
- Final check: `x == reversed_half` (even length) or `x == reversed_half // 10` (odd length).

- **Time Complexity:** O(log₁₀(n))  
- **Space Complexity:** O(1)  
- **Why this works:** By only processing half the digits, it avoids unnecessary work and preserves performance.

---

## 💡 Key Takeaways:
- **Cycle Detection:** When in doubt, use speed. Pointer-based traversal is a powerful tool in cyclic structures.
- **Math Insight:** Thinking in halves can halve your work — literally. Always ask: "Do I need the whole thing?"
