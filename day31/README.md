# 🚀 Day 31 – #DrGViswanathan 50 Days Coding Challenge

Today’s problems tackled **matrix manipulation** and **binary tree depth calculation**.

---

## 💫 Matrix Challenge: Flip and Invert Image (LeetCode 832)

### **Problem:**  
Given a binary matrix, flip each row horizontally, then invert the image (replace all 0s with 1s, and all 1s with 0s).

### **Approach:**  
Used a two-pointer approach to:
1. Swap elements from both ends of each row
2. Invert the values during the swap using bitwise XOR (`^ 1`)

### **Time Complexity:** O(n²)  
### **Space Complexity:** O(1)

### **Why this works:**  
This approach combines flipping and inverting in a single pass, reducing overhead and improving performance.

---

## 💫 Tree Challenge: Maximum Depth of Binary Tree (LeetCode 104)

### **Problem:**  
Given the root of a binary tree, return its maximum depth — the number of nodes along the longest path from the root node down to a leaf.

### **Approach:**  
Used recursion to:
1. Return 0 for null nodes (base case)  
2. Recursively calculate the left and right subtree depths  
3. Return `1 + max(left, right)`

### **Time Complexity:** O(n)  
### **Space Complexity:** O(h), where `h` is the height of the tree (due to the recursion stack)

### **Why this works:**  
Recursive traversal naturally fits the hierarchical structure of binary trees and helps simplify depth computation.

---

## 💡 Key Takeaways:

- Combining operations in-place (like flipping and inverting) improves both time and space efficiency.
- Recursive tree problems follow predictable patterns — mastering these builds a strong foundation for tackling more complex tree algorithms.
- Always start with a clear base case and work upwards when thinking recursively.


