# 🚀 Day 19 – #DrGViswanathan 50 Days Coding Challenge

Today we’re solving the balancing brackets and timing the stock market classic problems to strengthen your grasp on stacks and greedy logic.

---

## 💫 Stack Challenge: Valid Parentheses (LeetCode 20)

**Problem:**  
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. Open brackets must be closed by the same type of brackets and in the correct order.

**Approach:**  
Use a stack to track opening brackets. For every closing bracket, check if the top of the stack matches the corresponding opening bracket. If it doesn’t or stack is empty, return false. In the end, stack should be empty.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)  

**Why this works:**  
Stack ensures order and matching types are validated in one pass, maintaining correct bracket pairing.

---

## 💫 Greedy Challenge: Best Time to Buy and Sell Stock (LeetCode 121)

**Problem:**  
Given an array prices where prices[i] is the price of a stock on the ith day, find the maximum profit by buying and selling once.

**Approach:**  
Track the minimum price seen so far and calculate the profit if sold today. Update max profit accordingly.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)  

**Why this works:**  
By always buying at the lowest price and selling at a higher one, we maximize profit in a single pass.

---

## 💡 Key Takeaways:

- Stack is perfect for matching problems requiring order validation.  
- Greedy strategies shine in single-pass profit calculations.

