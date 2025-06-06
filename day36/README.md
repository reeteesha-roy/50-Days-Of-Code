# 🚀 Day 36 – #DrGViswanathan 50 Days Coding Challenge

Today’s problems tackled **root-to-leaf number sums** and **string vowel manipulation**.

---

## 💫 Tree Challenge: Sum Root to Leaf Numbers (LeetCode 129)

### **Problem:**  
Given a binary tree where each node contains a digit (0-9), each root-to-leaf path represents a number. Return the total sum of all these numbers.

### **Approach:**  
Used DFS recursion to:  
1. Keep track of the current number by accumulating digits (`current_number * 10 + node.val`)  
2. When reaching a leaf node, add the current number to the total sum  
3. Recurse through left and right children

### **Time Complexity:** O(n)  
### **Space Complexity:** O(h), where `h` is the height of the tree (due to recursion stack)

### **Why this works:**  
DFS naturally explores all root-to-leaf paths, and carrying forward the number makes it easy to compute values without extra storage.

---

## 💫 String Challenge: Reverse Vowels of a String (LeetCode 345)

### **Problem:**  
Given a string, reverse only the vowels (a, e, i, o, u, case-insensitive) and return the resulting string.

### **Approach:**  
Used two-pointer technique:  
1. Initialize pointers at start and end of the string  
2. Move pointers inward, swapping vowels when both pointers point to vowels  
3. Skip non-vowel characters

### **Time Complexity:** O(n)  
### **Space Complexity:** O(n) (due to converting string to list for in-place swaps)

### **Why this works:**  
Two-pointer approach efficiently reverses vowels in one pass without extra traversals.

---

## 💡 Key Takeaways:

- Carrying accumulated values through recursive calls is a slick way to solve root-to-leaf number problems.  
- Two-pointer techniques are super effective for in-place string manipulations, especially when focusing on subsets like vowels.  
- These patterns—DFS with state and two-pointer swaps—are essential tools in your coding toolkit.


