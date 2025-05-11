# 🚀 Day 7 – #DrGViswanathan 50 Days Coding Challenge

Today's theme: shifting gears in linked lists and handling number overflows without actual arithmetic.

---

## 💫 DSA Challenge: Rotate List (LeetCode 61)
**Problem:** Rotate a linked list to the right by `k` places.

### Approach:
1. **Calculate the length** of the list and find the tail.
2. **Optimize `k`** using modulo (`k % length`) to avoid unnecessary rotations.
3. **Find the new tail** (`length - k - 1` steps from the head) and set the next node as the new head.
4. Break the list and reconnect the tail to the original head.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)  
- **Why this works:** Smart use of modulo prevents wasted work. Rotating a list is just re-linking — no need for extra storage or data mutation.

---

## 💫 Math-based Challenge: Plus One (LeetCode 66)
**Problem:** Given an array of digits representing a non-negative integer, increment the number by one.

### Approach:
Iterated **backwards** through the list:
- If a digit is less than 9, increment it and return.
- If it's a 9, set it to 0 and continue.
- If the loop ends (e.g., `[9,9,9]`), prepend `1` to handle the carry.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1) (modifies in-place)  
- **Why this works:** Avoids converting to actual numbers or strings — it's all digit logic, clean and efficient.

---

## 💡 Key Takeaways:
- **Linked Lists:** Rotations are about rethinking structure, not shuffling data.
- **Array Math:** Knowing how and where to carry over in digit arrays avoids unnecessary conversions.
