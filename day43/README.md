# 🚀 Day 43 – #DrGViswanathan 50 Days Coding Challenge

Today's problems combined binary search tree traversal with simple array arithmetic, demonstrating tree navigation techniques and basic mathematical operations on arrays.

---

## 💫 Tree Challenge: Kth Smallest Element in a BST (LeetCode 230)

**Problem:**  
Given the root of a binary search tree and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

**Approach:**  
Use inorder traversal to leverage BST properties:
1. Perform inorder traversal (left → root → right) of the BST.
2. The inorder traversal of a BST visits nodes in ascending order.
3. Keep a counter during traversal and return the value when counter reaches k.
4. Can be implemented iteratively using a stack or recursively.

**Time Complexity:** O(H + k), where H is the height of the tree  
**Space Complexity:** O(H) for the recursion stack or explicit stack

**Why this works:**  
The inorder traversal of a BST naturally produces elements in sorted order. By stopping at the kth element during this traversal, we efficiently find the kth smallest without sorting the entire tree.

---

## 💫 Array Challenge: Plus One (LeetCode 66)

**Problem:**  
You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the ith digit of the integer. The digits are ordered from most significant to least significant. Increment the large integer by one and return the resulting array of digits.

**Approach:**  
Simulate addition with carry propagation:
1. Start from the rightmost digit (least significant).
2. Add 1 to the last digit.
3. If the result is less than 10, simply update and return.
4. If the result is 10, set current digit to 0 and carry 1 to the next position.
5. If all digits become 0 (e.g., 999 → 1000), create a new array with 1 followed by zeros.

**Time Complexity:** O(n), where n is the number of digits  
**Space Complexity:** O(1) or O(n) if we need to create a new array for overflow

**Why this works:**  
This mimics how we do addition by hand, handling carry propagation from right to left. The edge case of all 9's requires creating a longer array, which is handled by the overflow condition.

---

## 💡 Key Takeaways:
- Inorder traversal of BST provides elements in sorted order, making it perfect for finding kth smallest elements.
- Array manipulation problems often require careful handling of edge cases like overflow and boundary conditions.
