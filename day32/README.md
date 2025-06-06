# 🚀 Day 32 – #DrGViswanathan 50 Days Coding Challenge

Today’s problems tackled **binary tree level order traversal** and **matrix rotation**.

---

## 💫 Tree Challenge: Binary Tree Level Order Traversal (LeetCode 102)

### **Problem:**  
Given the root of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).

### **Approach:**  
Used Breadth-First Search (BFS) with a queue to:  
1. Traverse the tree level by level  
2. Collect nodes of each level into a separate list

### **Time Complexity:** O(n)  
### **Space Complexity:** O(n) (for the queue and result storage)

### **Why this works:**  
BFS naturally processes nodes level by level, perfectly fitting the requirement to gather nodes per depth level.

---

## 💫 Matrix Challenge: Rotate Image (LeetCode 48)

### **Problem:**  
Given an *n x n* 2D matrix representing an image, rotate the image by 90 degrees (clockwise) **in-place**.

### **Approach:**  
Used a two-step in-place approach:  
1. **Transpose** the matrix (swap `matrix[i][j]` with `matrix[j][i]`)  
2. **Reverse** each row to get the 90-degree rotated image

### **Time Complexity:** O(n²)  
### **Space Complexity:** O(1)

### **Why this works:**  
Transposing flips the matrix over its diagonal, and reversing each row completes the clockwise rotation without extra space.

---

## 💡 Key Takeaways:

- BFS is the go-to technique for level order tree traversal and can be easily implemented using a queue.  
- In-place matrix rotation can be efficiently done by combining transpose and row reversal — saves space without compromising clarity.  
- Mastering these patterns builds a strong foundation for solving complex matrix and tree problems.


