# 🚀 Day 41 – #DrGViswanathan 50 Days Coding Challenge

Today's problems focused on string manipulation and binary search tree operations, showcasing fundamental algorithms for text processing and tree traversal.

---

## 💫 String Challenge: Longest Common Prefix (LeetCode 14)

**Problem:**  
Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

**Approach:**  
Use vertical scanning to compare characters column by column:
1. If the array is empty, return an empty string.
2. Iterate through each character position of the first string.
3. For each position, check if all strings have the same character.
4. If a mismatch is found or we reach the end of any string, return the prefix found so far.

**Time Complexity:** O(S), where S is the sum of all characters in all strings  
**Space Complexity:** O(1)

**Why this works:**  
By comparing characters at the same position across all strings, we can efficiently find the longest common prefix without unnecessary string operations.

---

## 💫 Tree Challenge: Delete Node in a BST (LeetCode 450)

**Problem:**  
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference of the BST.

**Approach:**  
Handle three cases when deleting a node:
1. **Node has no children:** Simply remove it.
2. **Node has one child:** Replace the node with its child.
3. **Node has two children:** Find the inorder successor (smallest node in right subtree), replace the node's value with successor's value, then delete the successor.

**Time Complexity:** O(h), where h is the height of the tree  
**Space Complexity:** O(h), for the recursion stack

**Why this works:**  
The BST property must be maintained after deletion. The inorder successor is the smallest value greater than the current node, making it the perfect replacement that preserves BST ordering.

---

## 💡 Key Takeaways:
- Vertical scanning is an efficient approach for finding common prefixes in string arrays.
- BST deletion requires careful handling of different cases to maintain tree structure and ordering properties.
