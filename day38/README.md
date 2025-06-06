# 🚀 Day 38 – #DrGViswanathan 50 Days Coding Challenge

Today’s problems tackled **palindrome validation** and **BST node search**.

---

## 💫 String Challenge: Valid Palindrome (LeetCode 125)

### **Problem:**  
Given a string, determine if it’s a palindrome after converting uppercase letters to lowercase and removing all non-alphanumeric characters.

### **Approach:**  
Used two-pointer technique:  
1. Use pointers at start and end of string  
2. Move pointers inward, skipping non-alphanumeric characters  
3. Compare characters ignoring case  
4. Return false if mismatch found; true otherwise

### **Time Complexity:** O(n)  
### **Space Complexity:** O(1)

### **Why this works:**  
Two-pointer method efficiently validates palindrome without extra space for a cleaned string.

---

## 💫 Tree Challenge: Search in a Binary Search Tree (LeetCode 700)

### **Problem:**  
Given the root of a BST and a value `val`, find the node with value `val` and return the subtree rooted at that node. Return null if it doesn’t exist.

### **Approach:**  
Used BST property to traverse:  
1. If root is null or root value equals `val`, return root  
2. If `val` < root value, search left subtree  
3. Else, search right subtree

### **Time Complexity:** O(h), where `h` is height of the BST  
### **Space Complexity:** O(h) due to recursion stack

### **Why this works:**  
BST’s ordered structure allows pruning branches and efficient search.

---

## 💡 Key Takeaways:

- Two-pointer technique shines in palindrome and substring problems, cutting down space and complexity.  
- Leveraging BST properties makes search operations fast and clean.  
- Both problems show how structure-aware approaches simplify otherwise tricky tasks.


