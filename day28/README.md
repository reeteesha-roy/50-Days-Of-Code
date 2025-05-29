# 🚀 Day 28 – #DrGViswanathan 50 Days Coding Challenge

Another day, another dive into data structures and algorithms. Day 28 brought a mix of tree traversals and number theory that really kept the brain buzzing! Let’s get into it. 💡💻

---

## 💫 DSA Challenge 1: Minimum Depth of Binary Tree (LeetCode 111)

**Problem:** Given a binary tree, find its **minimum depth**—the shortest path from the root node to the nearest leaf node.

### Approach: Breadth-First Search (BFS)
1. **Start with the root** in a queue.
2. For each node:
   - Check if it’s a **leaf** (no left or right child).
   - If yes, return the depth.
   - If no, add its non-null children to the queue with incremented depth.
3. This ensures we find the shallowest leaf as soon as possible.

- **Time Complexity:** O(n) – where `n` is the number of nodes.
- **Space Complexity:** O(n) – for the queue used in BFS.
- **Why this works:** BFS is optimal for shortest-path problems like this, as it explores all nodes level-by-level.

---

## 💫 DSA Challenge 2: Count Subarrays with LCM Equal to K (LeetCode 2470)

**Problem:** Given an array `nums` and an integer `k`, count how many **contiguous subarrays** have a **least common multiple (LCM)** equal to `k`.

### Approach:
1. **Brute-Force with Smart Pruning:**
   - For each starting index `i`, initialize `curr_lcm = nums[i]`.
   - Skip `nums[i]` if `k % nums[i] != 0` (early pruning).
   - For every `j ≥ i`, update `curr_lcm = lcm(curr_lcm, nums[j])`.
   - If `curr_lcm == k`, count it.
   - If `curr_lcm > k`, break early.

2. **Helper Function:** Use `math.gcd()` to compute LCM via:

