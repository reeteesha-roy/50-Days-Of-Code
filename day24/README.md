# 🚀 Day 24 – #DrGViswanathan 50 Days Coding Challenge

Today's challenges leaned into **array manipulation mastery** and **expression parsing precision** utilizing  both iterative logic and stack-powered expression handling. 

---

## 💫 Array Challenge: Move Zeroes  
**LeetCode 283**

### 🧩 Problem  
Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

> You must do this in-place without making a copy of the array.

### 🛠️ Approach  
- Use a **two-pointer swap technique**:
  - One pointer (`non_zero_pos`) tracks where the next non-zero should go.
  - Iterate through the array:
    - If the element is non-zero, swap it with the value at `non_zero_pos`.
    - Increment `non_zero_pos`.
- This keeps non-zero elements in order and shifts zeros to the back.

### ⏱️ Time Complexity  
- `O(n)`

### 💾 Space Complexity  
- `O(1)` (in-place)

### ✅ Why This Works  
By only swapping non-zero elements forward, we naturally "bubble" all zeros to the end with minimal overhead — and no extra memory.

---

## 💫 String Challenge: Basic Calculator  
**LeetCode 224**

### 🧩 Problem  
Given a string `s` representing a valid mathematical expression (with `'+'`, `'-'`, `'('`, `')'`, digits, and spaces), evaluate and return the result.  

> Do **not** use `eval()` or similar built-ins!

### 🛠️ Approach  
- Use a **stack-based parser**:
  - Track `result`, `sign`, and `num` as you iterate through the string.
  - On `'('`: Push current result and sign to the stack.
  - On `')'`: Pop and combine with what's inside the parentheses.
  - On number: Build it digit by digit.
  - On `+` or `-`: Add the previous number with the correct sign to the result.
- Handle multi-digit numbers and ignore spaces.

### ⏱️ Time Complexity  
- `O(n)`

### 💾 Space Complexity  
- `O(n)` (stack for parentheses)

### ✅ Why This Works  
This approach mimics real arithmetic evaluation, stacking context when parentheses come in and unstacking it once they close. Clean, controlled, and totally `eval`-free 😎

---

## 💡 Key Takeaways

-  **Two-pointer strategies** are game-changers for in-place modifications in arrays.
-  **Stacks are essential** when parsing nested structures like parentheses in expressions.
-  Keeping track of just enough state (like current sign or previous result) helps you simulate complex operations simply.

