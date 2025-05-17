# 🚀 Day 18 – #DrGViswanathan 50 Days Coding Challenge  
Today we’re simulating queues using only stacks and tackling the classic duplicate detection in arrays. Two simple yet powerful problems to level up those data structure skills.

## 💫 Stack Simulation Challenge: Implement Queue using Stacks (LeetCode 232)  

### **Problem:**  
Implement a queue using only stack operations. The queue should support push(x), pop(), peek(), and empty().

### **Approach:**

- Use two stacks:  
  - `in_stack`: holds all newly pushed elements.  
  - `out_stack`: used when accessing elements in queue order.  
- On `push(x)`, add x to `in_stack`.  
- On `pop()` or `peek()`:  
  - If `out_stack` is empty, transfer all elements from `in_stack` to `out_stack` (reversing order).  
  - Then pop/peek from `out_stack`.  
- `empty()` returns True only if both stacks are empty.

### **Time Complexity:**   Amortized O(1) for all operations  
### **Space Complexity:**   O(n)

### **Why this works:**  
By deferring the reversal of elements until it’s absolutely needed, we efficiently simulate a queue using the raw power of stacks.

## 💫 Hash Set Challenge: Contains Duplicate (LeetCode 217)  

### **Problem:**  
Given an integer array `nums`, return true if any value appears at least twice. Return false if every element is distinct.

### **Approach:**

- Use a set `seen` to track numbers encountered so far.  
- Loop through the array:  
  - If the number is already in `seen`, return True.  
  - Otherwise, add it to `seen`.  
- If the loop ends, return False.

### **Time Complexity:** O(n)  
### **Space Complexity:** O(n)

### **Why this works:**  
Sets provide O(1) lookups, so this approach avoids nested loops and gives us a clean, efficient solution.

## 💡 Key Takeaways:  

- Queue Logic with Stacks: It’s all about reversing flow only when necessary. Efficient use of two stacks gets the job done.

-  Duplicate Detection:  Tracking what's been seen saves time and avoids unnecessary scans.

