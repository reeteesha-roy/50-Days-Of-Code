# 🚀 Day 10 – #DrGViswanathan 50 Days Coding Challenge

 Today’s tasks were about cutting out the middle (literally) and flipping bulbs with some math flair.

---

## 💫 DSA Challenge: Delete the Middle Node of a Linked List (LeetCode 2095)
**Problem:** Given the head of a singly linked list, delete the middle node and return the modified list.

### Approach:
1. **Edge case:** If the list has only one node, return `None`.
2. **First pass:** Calculate the total length.
3. **Second pass:** Navigate to the node just before the middle and adjust the `next` pointer to skip the middle node.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)  
- **Why this works:** Middle index is deterministically `length // 2`, and two simple passes keep it readable and safe.

---

## 💫 Math-based Challenge: Bulb Switcher (LeetCode 319)
**Problem:** You have `n` bulbs. All start off. Each round `i`, you toggle every `i`th bulb. How many bulbs are on after `n` rounds?

### Approach:
1. **Brute-force intuition:** Simulate toggling — each bulb toggles on every divisor it has.
2. **Math insight:** A bulb ends **on** if it is toggled an odd number of times.
3. **Key realization:** Only perfect squares have an odd number of divisors (because one divisor is repeated).
4. **Final logic:** Count how many perfect squares ≤ `n`, which is just `int(sqrt(n))`.

- **Time Complexity:** O(1)  
- **Space Complexity:** O(1)
-  **Why this works:** Once you get the math behind the toggles, it becomes a simple square root problem.

---

## 💡 Key Takeaways:
- **Linked Lists:** Double-pass is still efficient and great for cases where random access isn’t possible.
- **Math Problems:** Recognizing patterns in number theory turns simulations into instant answers.


