# 🚀 Day 35 – #DrGViswanathan 50 Days Coding Challenge

Today’s problems tackled **lowest common ancestor in trees** and **string segment counting**.

---

## 💫 Tree Challenge: Lowest Common Ancestor of a Binary Tree (LeetCode 236)

### **Problem:**  
Given the root of a binary tree and two nodes `p` and `q`, find their lowest common ancestor (LCA). The LCA is the lowest node in the tree that has both `p` and `q` as descendants (a node can be a descendant of itself).

### **Approach:**  
Used recursion to:  
1. Return the current node if it matches `p` or `q`  
2. Recursively search left and right subtrees  
3. If both sides return non-null, current node is LCA  
4. Otherwise, return the non-null child

### **Time Complexity:** O(n)  
### **Space Complexity:** O(h), where `h` is the height of the tree (due to recursion stack)

### **Why this works:**  
The recursive search efficiently bubbles up found nodes and identifies the split point where `p` and `q` diverge, which is the LCA.

---

## 💫 String Challenge: Number of Segments in a String (LeetCode 434)

### **Problem:**  
Given a string `s`, return the number of segments in the string. A segment is defined as a contiguous sequence of non-space characters.

### **Approach:**  
Used string splitting and filtering:  
1. Split the string by spaces  
2. Count non-empty segments

### **Time Complexity:** O(n)  
### **Space Complexity:** O(n) (due to splitting)

### **Why this works:**  
Splitting by spaces isolates segments, and filtering out empty strings handles multiple or trailing spaces.

---

## 💡 Key Takeaways:

- Recursive traversal is a natural fit for LCA problems, helping identify the common ancestor without extra data structures.  
- Simple string operations are often enough for segment counting, avoiding complicated parsing logic.  
- Both problems highlight the power of clean recursion and basic string manipulation techniques.


