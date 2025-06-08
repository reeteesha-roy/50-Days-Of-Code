# 🚀 Day 40 – #DrGViswanathan 50 Days Coding Challenge

Today we’re tackling two super useful problems: checking if a string can become another via rotations, and finding the lowest common ancestor in a binary search tree using its structural properties.

---

### 💫 String Challenge: Rotate String (LeetCode 796)

**Problem:**  
Given two strings `s` and `goal`, return `true` if and only if `s` can become `goal` after some number of shifts.  
A shift moves the leftmost character of `s` to the rightmost position.

**Approach:**

- Check if lengths of `s` and `goal` are the same.
- Concatenate `s` with itself → this contains all possible rotations.
- Return `True` if `goal` is a substring of `s + s`.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

**Why this works:**  
By doubling the string, we contain every possible rotated version of `s`. If `goal` is in there, we’re golden.

---

### 💫 Tree Challenge: Lowest Common Ancestor in BST (LeetCode 235)

**Problem:**  
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes `p` and `q`.  
The LCA is the lowest node that has both `p` and `q` as descendants.

**Approach:**

- Start from the root.
- If both `p` and `q` are greater than the root, go right.
- If both are smaller, go left.
- If they split (or one matches root), current node is the LCA.

**Time Complexity:** O(h), where h = height of the tree  
**Space Complexity:** O(1) iterative, O(h) if recursive

**Why this works:**  
In a BST, the left subtree has smaller values, right has larger. So we can navigate smartly without scanning everything.

---

### 💡 Key Takeaways:

🌀 **String Rotation:**  
A creative trick like `s + s` can turn a seemingly tough rotation check into a one-liner.

🌳 **BST Navigation:**  
BST structure lets us zoom in on answers without searching the entire tree. Efficient and elegant!

