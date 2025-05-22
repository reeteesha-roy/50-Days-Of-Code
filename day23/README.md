# 🚀 Day 23 – #DrGViswanathan 50 Days Coding Challenge

Today's challenges focused on **binary search precision** and **navigating well-formed strings** — two core DSA concepts that blend efficiency and string structure handling.

---

## 💫 Array Challenge: Search Insert Position  
**LeetCode 35**

### 🧩 Problem  
Given a sorted array of distinct integers and a target value, return the index if the target is found.  
If not, return the index where it would be inserted in order to maintain the sort.

### 🛠️ Approach  
- Use **Binary Search**:
  - Initialize `left` and `right` pointers.
  - Calculate the middle index.
  - Compare the middle element with the target.
  - Narrow the search window accordingly.
- If the target is not found, return `left` as the insert position.

### ⏱️ Time Complexity  
- `O(log n)`

### 💾 Space Complexity  
- `O(1)`

### ✅ Why This Works  
Binary Search efficiently narrows down the position of the target (or insertion point) by halving the array each step, giving optimal performance for sorted arrays.

---

## 💫 String Challenge: Longest Valid Parentheses  
**LeetCode 32**

### 🧩 Problem  
Given a string containing just `'('` and `')'`, return the length of the longest valid (well-formed) parentheses substring.

### 🛠️ Approach  
- Use a **stack** to track the indices:
  - Initialize stack with `-1` as a base index.
  - For `'('`, push the index onto the stack.
  - For `')'`, pop the stack:
    - If the stack becomes empty, push current index.
    - Else, calculate the length: `i - stack[-1]`.
  - Keep track of the **maximum length** found.

### ⏱️ Time Complexity  
- `O(n)`

### 💾 Space Complexity  
- `O(n)`

### ✅ Why This Works  
The stack helps track the position of unmatched `'('`, and calculating `i - stack[-1]` gives the length of each valid substring as we go.

---

## 💡 Key Takeaways

- 🧠 **Binary Search** is your best friend when dealing with sorted arrays and insertion logic.
- 🧵 **Stack-based indexing** is a powerful tool for validating structured strings like parentheses.
- 🧰 Tracking base cases (like `-1` in the stack) can simplify edge-case handling and make your logic cleaner.

