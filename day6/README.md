# 🚀 Day 6 – #DrGViswanathan 50 Days Coding Challenge

Getting surgical with node removals and chasing happiness with cycle detection in numbers. 🧠💫

---

## 💫 DSA Challenge: Remove Linked List Elements (LeetCode 203)
**Problem:** Remove all elements from a linked list that have a specific value.

### Approach:
Used a **dummy node** as a new head to simplify edge case handling (like when the head needs to be removed). 
Iterated through the list with a `current` pointer:
- If `current.next` matches the target value, it's skipped.
- Otherwise, moved forward.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)  
- **Why this works:** The dummy node removes the need for extra checks at the head, keeping the logic clean and efficient.

---

## 💫 Math-based Challenge: Happy Number (LeetCode 202)
**Problem:** Determine if a number eventually reaches 1 when replaced repeatedly by the sum of the squares of its digits.

### Approach:
Applied **Floyd’s Cycle Detection Algorithm**:
- Created a helper function to get the sum of squares of digits.
- Used `slow` and `fast` pointers to detect cycles.
- If the fast pointer hits 1, it’s a happy number.
- If it loops, it’s not.

- **Time Complexity:** O(log n) per cycle step  
- **Space Complexity:** O(1)  
- **Why this works:** Instead of using a set to track seen numbers, cycle detection keeps it memory-efficient while reliably identifying loops.

---

## 💡 Key Takeaways:
- **Linked Lists:** Dummy nodes continue to prove themselves as MVPs in structural edits.
- **Math Puzzles:** Cycle detection isn't just for lists — it shows up in number transformations too.
