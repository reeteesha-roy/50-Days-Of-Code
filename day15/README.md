# 🚀 Day 15 – #DrGViswanathan 50 Days Coding Challenge  
Today, we tackle problems related to finding the longest substring without repeating characters and converting a given integer to its corresponding Excel column title. Let’s dive into these challenges!

## 💫 DSA Challenge: Add Two Numbers (LeetCode 2)  
**Problem:**  
Given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each node contains a single digit. Add the two numbers and return the sum as a linked list.

### Approach:
- Initialize a dummy head node to build the result linked list.
- Use two pointers to traverse the input linked lists.
- Keep track of carry from the sum of digits.
- For each pair of nodes, sum their values along with the carry.
- Create a new node with the digit value of the sum modulo 10.
- Update carry as the sum divided by 10.
- Continue until both lists are fully traversed and carry is zero.

**Time Complexity:** O(max(m, n)), where m and n are the lengths of the two lists.  
**Space Complexity:** O(max(m, n)), for the output list.

**Why this works:**  
By simulating elementary addition digit by digit with carry, this approach effectively sums two numbers represented as linked lists in reverse order.


## 💫 Math-based Challenge: Convert Integer to Excel Column Title (LeetCode 168)  
**Problem:** Given an integer `columnNumber`, return its corresponding column title as it appears in an Excel sheet.

### Approach:
- Think of the column number in a base-26 system, but adjust for the fact that Excel columns are 1-indexed.
- Repeatedly divide the `columnNumber` by 26 to get the corresponding character for the current "digit" in the column title.
- For each division, find the remainder, which corresponds to a letter (A-Z).
- After finding the corresponding letter, update `columnNumber` and repeat the process until the entire title is constructed.
  
**Time Complexity:** O(log n), where n is the column number.  
**Space Complexity:** O(1) — no extra space is needed apart from a few variables for the process.

**Why this works:** By handling the column number similarly to a base-26 system while accounting for 1-based indexing, we can map numbers to their Excel column titles efficiently.

## 💡 Key Takeaways:  
- **Sliding Window:** A powerful technique to solve problems involving substrings or subarrays while maintaining certain constraints (like uniqueness).  
- **Base Conversion:** Understanding how to convert between number systems (like base-10 to base-26) and how it relates to real-world problems (like Excel columns) can help simplify complex tasks.

