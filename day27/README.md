# 🚀 Day 27 – #DrGViswanathan 50 Days Coding Challenge

Another day, another set of challenges. Let’s dive right in! 

---

## 💫  Has Path Sum (LeetCode 112)

**Problem:** Given the root of a binary tree and an integer `targetSum`, return `true` if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`.

### Approach:
1. **Base Case Check:** If the node is `None`, return `False`.
2. **Leaf Node Check:** If it’s a leaf, check if the node value equals the remaining `targetSum`.
3. **Recursive Step:** Subtract the current node's value from `targetSum` and recursively check the left and right subtrees.

- **Time Complexity:** O(n) – where `n` is the number of nodes in the tree.
- **Space Complexity:** O(h) – where `h` is the height of the tree due to recursion stack.
- **Why this works:** It leverages depth-first search to explore each possible path from root to leaf.

---

## 💫  Maximum Subarray (LeetCode 53)

**Problem:** Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the **largest sum**, and return its sum.

### Approach: Kadane’s Algorithm
1. **Initialize Two Variables:**
   - `curr_sum` to track the best subarray *ending* at the current index.
   - `max_sum` to store the best subarray *seen so far*.

2. **Iterate Through the Array:**
   - At each element, decide whether to continue with the current subarray or start fresh.
   - Update `max_sum` accordingly.

3. **Return `max_sum`** after the loop.

- **Time Complexity:** O(n) – One pass through the array.
- **Space Complexity:** O(1) – No extra space required.
- **Why this works:** It efficiently tracks local and global maxima without brute-forcing every subarray.

---

## 💡 Key Takeaways:
- **Tree Traversal Logic:** Recursive depth-first search is a powerful tool when exploring paths and conditions in trees.
- **Greedy + DP Magic:** Kadane's Algorithm is a brilliant example of dynamic programming in disguise—simple logic, big impact.
- **Keep it Efficient:** Knowing when to use recursion vs iteration and greedy vs brute-force can massively cut down execution time.
