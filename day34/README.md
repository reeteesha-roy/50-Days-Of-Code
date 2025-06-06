# 🚀 Day 34 – #DrGViswanathan 50 Days Coding Challenge

Today’s problems tackled **binary tree flattening** and **string manipulation**.

---

## 💫 Tree Challenge: Flatten Binary Tree to Linked List (LeetCode 114)

### **Problem:**  
Given the root of a binary tree, flatten it to a “linked list” in-place. The linked list should follow the same order as a pre-order traversal, with all left pointers set to null.

### **Approach:**  
Used a recursive reverse pre-order traversal:  
1. Recursively flatten right and left subtrees  
2. Keep track of the previously processed node  
3. Set the current node’s right to the previous node and left to null

### **Time Complexity:** O(n)  
### **Space Complexity:** O(h), where `h` is the height of the tree (due to recursion stack)

### **Why this works:**  
Reverse pre-order traversal ensures the right child is processed first, allowing us to link nodes correctly to form a flattened list in pre-order.

---

## 💫 String Challenge: Length of Last Word (LeetCode 58)

### **Problem:**  
Given a string `s` consisting of words and spaces, return the length of the last word in the string.

### **Approach:**  
Used string trimming and splitting:  
1. Strip trailing spaces  
2. Split the string by spaces  
3. Return the length of the last word

### **Time Complexity:** O(n)  
### **Space Complexity:** O(n) (due to splitting)

### **Why this works:**  
Stripping ensures no empty strings at the end, and splitting isolates words for easy length calculation.

---

## 💡 Key Takeaways:

- Recursive tree flattening can be elegantly solved with reverse pre-order traversal and tracking previously visited nodes.  
- Simple string operations like trimming and splitting make word-based problems straightforward and efficient.  
- Combining traversal techniques with careful pointer updates is a powerful approach in tree problems.


