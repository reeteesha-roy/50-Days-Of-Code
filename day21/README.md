# 🚀 Day 21 – #DrGViswanathan 50 Days Coding Challenge

Wildcard brackets and Pascal’s Triangle brought some fresh twists and elegant patterns today.

---

## 💫 Stack & Greedy Challenge: Valid Parenthesis String (LeetCode 678)

**Problem:**  
Given a string containing '(', ')', and '*', check if it’s valid. '*' can represent '(', ')', or an empty string.

**Approach:**  
Track a range [low, high] of possible open parentheses counts as you scan. Adjust bounds for each character, and ensure validity by the end.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)  

**Why this works:**  
Maintaining low and high counts simulates all interpretations of '*' without backtracking.

---

## 💫 Math Challenge: Pascal’s Triangle II (LeetCode 119)

**Problem:**  
Return the kth (0-indexed) row of Pascal’s Triangle.

**Approach:**  
Build the row iteratively using previous values or use combinatorial math.

**Time Complexity:** O(k²) or O(k) with combinatorics  
**Space Complexity:** O(k)  

**Why this works:**  
Each element depends on the sum of two elements above it, producing beautiful number patterns.

---

## 💡 Key Takeaways:

- Creative range tracking solves ambiguous bracket problems efficiently.  
- Pascal’s Triangle reveals deep connections between combinatorics and recursion.

