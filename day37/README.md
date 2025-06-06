# 🚀 Day 37 – #DrGViswanathan 50 Days Coding Challenge

Today’s problems tackled **zigzag traversal of binary trees** and **palindromic string detection**.

---

## 💫 Tree Challenge: Binary Tree Zigzag Level Order Traversal (LeetCode 103)

### **Problem:**  
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. That means the first level is left-to-right, the second right-to-left, and so on, alternating with each level.

### **Approach:**  
Used BFS with a queue to:  
1. Traverse level by level  
2. Reverse the order of nodes at every alternate level before adding to result

### **Time Complexity:** O(n)  
### **Space Complexity:** O(n) (for queue and result)

### **Why this works:**  
Level-order traversal ensures nodes are processed per depth, and reversing on alternate levels creates the zigzag pattern efficiently.

---

## 💫 String Challenge: Find First Palindromic String in the Array (LeetCode 2108)

### **Problem:**  
Given an array of strings, return the first palindromic string. If none exist, return an empty string.

### **Approach:**  
Iterate through the array and check each string:  
1. Check if string equals its reverse  
2. Return the first palindrome found

### **Time Complexity:** O(n * m), where `n` is number of strings and `m` is average string length  
### **Space Complexity:** O(m) for string reversal

### **Why this works:**  
String reversal is a straightforward way to verify palindromes, and early return optimizes for the first occurrence.

---

## 💡 Key Takeaways:

- Zigzag traversal is just a twist on BFS—flip the order of nodes every other level to change direction.  
- Checking palindromes by reversing strings is simple and effective for string array problems.  
- Combining traversal patterns with condition checks leads to clean, efficient solutions.


