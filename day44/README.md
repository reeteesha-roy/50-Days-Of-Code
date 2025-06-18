# 🚀 Day 44 – #DrGViswanathan 50 Days Coding Challenge

Today's problems involved converting sorted data structures to balanced trees and string processing with sliding window techniques, showcasing tree construction algorithms and substring optimization.

---

## 💫 Tree Challenge: Convert Sorted List to Binary Search Tree (LeetCode 109)

**Problem:**  
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

**Approach:**  
Use divide and conquer with inorder simulation:
1. **Method 1 - Convert to Array:** Convert linked list to array, then use binary search approach to build BST.
2. **Method 2 - Inorder Simulation:** Use two pointers to find middle, recursively build left subtree, create root, then build right subtree.
3. **Method 3 - Bottom-up Construction:** Simulate inorder traversal while building the tree from bottom up.

**Time Complexity:** O(n)  
**Space Complexity:** O(log n) for recursion stack in balanced tree

**Why this works:**  
Since the linked list is sorted, the middle element should be the root for balance. Recursively applying this principle to sublists ensures a height-balanced BST. The inorder simulation approach is most efficient as it processes each node exactly once.

---

## 💫 String Challenge: Maximum Number of Vowels in a Substring (LeetCode 1456)

**Problem:**  
Given a string `s` and an integer `k`, return the maximum number of vowel letters in any substring of `s` with length `k`.

**Approach:**  
Use sliding window technique:
1. Define vowels set: {'a', 'e', 'i', 'o', 'u'}.
2. Count vowels in the first window of size k.
3. Slide the window by removing the leftmost character and adding the rightmost character.
4. Update the vowel count accordingly and track the maximum.
5. Continue until the window reaches the end of the string.

**Time Complexity:** O(n), where n is the length of the string  
**Space Complexity:** O(1)

**Why this works:**  
The sliding window technique avoids recalculating the entire substring count. By incrementally updating the vowel count as we slide the window, we achieve optimal time complexity while maintaining the fixed window size constraint.

---

## 💡 Key Takeaways:
- Converting sorted structures to balanced trees requires careful middle-element selection and recursive construction.
- Sliding window technique is optimal for fixed-size substring problems, avoiding redundant calculations.
