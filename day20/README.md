# 🚀 Day 20 – #DrGViswanathan 50 Days Coding Challenge

Today we tackled number theory and expression evaluation. Both highlight how math and stacks collide in problem-solving.

---

## 💫 Math Challenge: Greatest Common Divisor of Smallest and Largest Number (LeetCode 1979)

**Problem:**  
Given an integer array nums, return the greatest common divisor of the smallest and largest numbers in the array.

**Approach:**  
Find min and max of the array, then compute gcd using Euclidean algorithm or built-in function.

**Time Complexity:** O(n) (for min and max)  
**Space Complexity:** O(1)  

**Why this works:**  
GCD of min and max gives a neat number-theoretic insight into the array extremes.

---

## 💫 Stack Challenge: Evaluate Reverse Polish Notation (LeetCode 150)

**Problem:**  
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Supported operators: +, -, *, / (integer division truncating toward zero).

**Approach:**  
Use a stack to store numbers. On operator, pop two numbers, apply operator, and push result back.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)  

**Why this works:**  
Stacks are natural for evaluating postfix expressions because operands come before operators.

---

## 💡 Key Takeaways:

- Math functions can simplify what looks complex.  
- Stack-based evaluation of expressions is efficient and clean.

