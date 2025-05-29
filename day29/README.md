# 🚀 Day 29 – #DrGViswanathan 50 Days Coding Challenge

Day 29 vibes: digging into some tree leaf sums and heap magic for kth largest elements. Let's roll! 

---

## 💫 DSA Challenge 1: Sum of Left Leaves (LeetCode 404)

**Problem:** Given the root of a binary tree, return the sum of all **left leaves**. A left leaf is a leaf node that is the left child of its parent.

### Approach:
1. **Check if Left Child is Leaf:**  
   - If yes, add its value to the sum.
2. **Recursively Traverse:**  
   - Visit left and right children to find other left leaves.
3. **Accumulate Total Sum.**

- **Time Complexity:** O(n) – visit each node once.  
- **Space Complexity:** O(h) – recursion stack, where `h` is the tree height.  
- **Why this works:** A simple recursive check at each node to capture left leaves only.

---

## 💫 DSA Challenge 2: Kth Largest Element in an Array (LeetCode 215)

**Problem:** Find the kth largest element in an unsorted array without sorting the entire array.

### Approach: Min-Heap of size k
1. **Use a min-heap to keep track of k largest elements.**
2. **Iterate through nums:**  
   - Push current element into heap.  
   - If heap size > k, pop smallest element.
3. **The root of the heap is the kth largest element.**

- **Time Complexity:** O(n log k) – each insertion and removal costs O(log k).  
- **Space Complexity:** O(k) – heap size.  
- **Why this works:** Keeps only the top k largest elements efficiently.

---

## 💡 Key Takeaways:
- **Selective Traversal:** For tree problems, focusing on specific child nodes can simplify what to sum or count.
- **Data Structures FTW:** Using heaps cleverly can save you from sorting overhead and keep your code lean and fast.
- **Practice Makes Perfect:** These patterns (leaf checks, min heaps) pop up all over — get comfy with them now.
