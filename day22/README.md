# 🚀 Day 22 – #DrGViswanathan 50 Days Coding Challenge

Today’s challenges focused on majority element detection and cleaning up invalid parentheses — classic problems that combine clever logic with string and array manipulation.

---

## 💫 Array Challenge: Majority Element (LeetCode 169)

**Problem:**  
Given an array `nums` of size `n`, return the majority element — the element that appears more than ⌊n / 2⌋ times. You may assume the majority element always exists.

**Approach:**  
Use the Boyer-Moore Voting Algorithm:  
- Initialize a candidate and a count.  
- Iterate through the array, update candidate when count drops to zero.  
- Increment or decrement count based on current element matching candidate.  
- Return candidate after one pass.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)  

**Why this works:**  
By balancing increments and decrements, the candidate that remains is the majority element.

---

## 💫 String Challenge: Minimum Remove to Make Valid Parentheses (LeetCode 1249)

**Problem:**  
Given a string `s` containing '(', ')', and lowercase letters, remove the minimum number of parentheses to make the string valid.

**Approach:**  
- Use a stack to track indices of '(' characters.  
- When encountering ')', pop from stack if possible; else mark ')' for removal.  
- After one pass, remove any unmatched '(' left in the stack.  
- Join the filtered characters to form the valid string.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)  

**Why this works:**  
Tracking indices allows us to remove only invalid parentheses efficiently, preserving the rest of the string.

---

## 💡 Key Takeaways:

- Boyer-Moore Voting is a slick O(1) space solution for majority element problems.  
- Stack-based indexing is super helpful for validating and cleaning parentheses in strings.
