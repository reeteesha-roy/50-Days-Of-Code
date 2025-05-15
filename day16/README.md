# 🚀 Day 16 – #DrGViswanathan 50 Days Coding Challenge

Today we’re tackling classic linked list manipulation and exploring whether a number can be represented as the sum of two squares.

---

## 💫 Linked List Challenge: Delete Node in a Linked List (LeetCode 237)

**Problem:**  
You are given a node in a singly-linked list that is **not the tail**, but you’re **not given access to the head**. Delete the node so that its value should no longer exist in the list, and the list should remain valid.

**Approach:**
- Copy the value from the **next node** into the current node.
- Skip the next node by pointing `node.next` to `node.next.next`.

**Time Complexity:** O(1)  
**Space Complexity:** O(1)

**Why this works:**  
We're not really deleting the node overwriting it with the next node and cutting the next node out of the list. 

---

## 💫 Math-based Challenge: Sum of Square Numbers (LeetCode 633)

**Problem:**  
Given a non-negative integer `c`, determine whether there are two integers `a` and `b` such that:  
\[
a^2 + b^2 = c
\]

**Approach:**
- Iterate `a` from 0 to `√c`.
- For each `a`, compute `b² = c - a²`.
- If `b²` is a **perfect square**, we’ve got our answer — return `True`.
- If the loop ends with no match, return `False`.

**Time Complexity:** O(√c)  
**Space Complexity:** O(1)

**Why this works:**  
We're leveraging the fact that we only need to check up to `√c`, and checking perfect squares is super efficient with `math.sqrt()` + integer comparison. Clean, fast, and mathematically sound. 📐🔥

---

## 💡 Key Takeaways:

🧩 **Linked Lists:**  
Copy + skip can be all you need when node access is limited.

🧠 **Math Checks:**  
Breaking a number down into squares is a classic way to flex your number theory and efficient iteration game.

