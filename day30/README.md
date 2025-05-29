# 🚀 Day 30 – #DrGViswanathan 50 Days Coding Challenge

Today’s problems got us thinking about cycles and diameters which are classic brain teasers that sharpen your algorithm skills. 

---

## 💫 DSA Challenge 1: Diameter of Binary Tree (LeetCode 543)

**Problem:** Find the length of the longest path (diameter) between any two nodes in a binary tree. This path may or may not pass through the root.

### Approach:
1. Use a **DFS** helper to calculate the height of each node’s subtree.
2. At each node, update the maximum diameter as the sum of left and right subtree heights.
3. The final maximum diameter tracked is the answer.

- **Time Complexity:** O(n) – each node visited once.  
- **Space Complexity:** O(h) – recursion stack, where `h` is tree height.  
- **Why this works:** Height-based DFS lets us find the longest path going through any node efficiently.

---

## 💫 DSA Challenge 2: Find the Duplicate Number (LeetCode 287)

**Problem:** Given an array containing `n + 1` integers where each integer is between `1` and `n`, find the single duplicate number without modifying the array or using extra space.

### Approach: Floyd’s Tortoise and Hare (Cycle Detection)
1. Treat array indices and values like a linked list with a cycle.
2. Use two pointers moving at different speeds to detect a cycle.
3. Find the entry point of the cycle — which corresponds to the duplicate number.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)  
- **Why this works:** The duplicate creates a cycle in the “linked list” formed by array elements.

---

## 💡 Key Takeaways:
- **DFS for Diameter:** Height calculations can unlock insights about tree paths beyond just depth.
- **Cycle Detection in Arrays:** Clever transformations (array → linked list) open doors to classic algorithms in unusual places.
- **Optimization Matters:** Constraints (no modification, O(1) space) push us to think beyond brute force.

