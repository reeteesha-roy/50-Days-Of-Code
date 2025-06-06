# 🚀 Day 33 – #DrGViswanathan 50 Days Coding Challenge

Today’s problems tackled **binary tree right side view** and **array manipulation with LCM and GCD**.

---

## 💫 Tree Challenge: Binary Tree Right Side View (LeetCode 199)

### **Problem:**  
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

### **Approach:**  
Used level-order traversal (BFS) with a queue to:  
1. Traverse the tree level by level  
2. Capture the last node’s value at each level (the rightmost visible node)

### **Time Complexity:** O(n)  
### **Space Complexity:** O(n) (for the queue and output list)

### **Why this works:**  
Level-order traversal lets us easily identify the rightmost node at each depth, which corresponds to what’s visible from the right side.

---

## 💫 Array Challenge: Replace Non-Coprime Numbers in Array (LeetCode 2197)

### **Problem:**  
Given an array of integers, repeatedly replace any two adjacent non-coprime numbers with their LCM until no such pairs remain. Return the resulting array.

### **Approach:**  
Used a stack to process numbers:  
1. For each number, check if the top of the stack is non-coprime (GCD > 1)  
2. If yes, pop the top and replace both with their LCM  
3. Repeat merges until top and current number are coprime  
4. Push the final merged number to the stack

### **Time Complexity:** O(n log(max(nums))) (due to GCD computations)  
### **Space Complexity:** O(n)

### **Why this works:**  
Using a stack to merge on the fly ensures that all adjacent non-coprime pairs are handled efficiently, and the final result is unique regardless of merge order.

---

## 💡 Key Takeaways:

- BFS is perfect for problems involving “views” or level-based visibility in trees.  
- Stack-based merging combined with GCD/LCM calculations elegantly solves complex array transformation problems.  
- Understanding how to efficiently compute and apply GCD and LCM can unlock solutions to tricky number theory problems.


