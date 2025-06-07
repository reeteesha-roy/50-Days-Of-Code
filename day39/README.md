# 🚀 Day 39 – #DrGViswanathan 50 Days Coding Challenge

Today’s problems involved binary search trees and string cleaning using stack-like logic.

---

## 💫 Tree Challenge: Insert into a Binary Search Tree (LeetCode 701)

**Problem:**  
Given the root of a Binary Search Tree (BST) and an integer value `val`, insert the value into the BST such that it remains a valid BST. Return the root of the updated tree.

**Approach:**  
Use a simple recursive strategy:
1. If the current node is `None`, return a new TreeNode with `val`.
2. If `val` is less than the node's value, recurse left.
3. Otherwise, recurse right.

**Time Complexity:** O(h), where h is the height of the tree  
**Space Complexity:** O(h), for the recursion stack

**Why this works:**  
A BST follows strict ordering rules. Recursively placing the new value preserves structure and ensures that all left descendants are smaller, and all right descendants are greater.

---

## 💫 Stack Challenge: Remove All Adjacent Duplicates in String (LeetCode 1047)

**Problem:**  
Given a string `s`, repeatedly remove pairs of adjacent duplicate characters until no more adjacent duplicates exist. Return the final string.

**Approach:**  
Use a stack to track non-duplicate characters:
1. Loop through each character in the string.
2. If the top of the stack equals the current character, pop it.
3. Otherwise, push the character onto the stack.
4. Join the stack to form the result.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)  

**Why this works:**  
A stack perfectly models the problem’s requirement: last-in, first-out. By removing characters as soon as a pair is formed, we keep the string clean and efficient to process.

---

## 💡 Key Takeaways:

- Recursion is used when navigating hierarchical data structures like trees.  
- Stacks are powerful for real-world string processing.  

