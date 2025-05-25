# 🚀 Day 26 – #DrGViswanathan 50 Days Coding Challenge

Today’s problems tackled **binary search** precision and **binary tree traversal**.

---

## 💫 Search Challenge: Find First and Last Position of Element in Sorted Array (LeetCode 34)

**Problem:**  
Given a sorted array of integers `nums` and a target value, return the starting and ending position of the target.  
If the target is not found, return `[-1, -1]`.

**Approach:**  
Use **binary search** twice:
1. First binary search to find the **leftmost** occurrence.
2. Second binary search to find the **rightmost** occurrence.

**Time Complexity:** O(log n)  
**Space Complexity:** O(1)

**Why this works:**  
Binary search narrows down the search space efficiently. By continuing the search even after finding the target, we lock onto the boundaries precisely.

---

## 💫 Tree Challenge: Binary Tree Inorder Traversal (LeetCode 94)

**Problem:**  
Given the root of a binary tree, return its inorder traversal (left → root → right).

**Approach:**  
Used a **recursive helper function** to:
1. Traverse the left subtree  
2. Visit the current node  
3. Traverse the right subtree

**Time Complexity:** O(n)  
**Space Complexity:** O(n) for the call stack (in worst case of skewed tree)

**Why this works:**  
Recursion naturally models the tree structure, making the traversal intuitive and clean to implement.

---

## 💡 Key Takeaways:

- Binary search isn’t just about finding a value — it can find **positions**, **ranges**, and **boundaries** with tweaks.
- Tree traversal patterns (inorder, preorder, postorder) are essential building blocks for many tree-based problems.
- Understanding algorithm patterns lets you solve problems confidently and optimally.
