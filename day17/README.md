# 🚀 Day 17 – #DrGViswanathan 50 Days Coding Challenge

Today we’re diving into two core DSA problems: designing a custom stack that tracks minimums in real-time, and using hash maps to crack the all-time classic problem—Two Sum. 

---

### 💫 Stack Challenge: Min Stack (LeetCode 155)

**Problem:**  
Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in **constant time**.

**Approach:**

- Maintain two stacks:
  - `stack`: holds all pushed values.
  - `min_stack`: tracks the current minimum at each level.
- On `push`, also push to `min_stack` if it’s the new minimum.
- On `pop`, remove from both if the top of the stack is the current min.
- `top()` returns the last element of `stack`.
- `getMin()` returns the last element of `min_stack`.

**Time Complexity:** O(1) for all operations  
**Space Complexity:** O(n) extra stack for mins

**Why this works:**  
By shadowing every push with a minimum tracker, we make `getMin()` instant. This is a perfect example of trading a little space for blazing speed. 

---

### 💫 Hash Map Challenge: Two Sum (LeetCode 1)

**Problem:**  
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.  
Each input has exactly one solution, and you may not use the same element twice.

**Approach:**

- Use a dictionary `num_map` to store each number's index.
- Loop through `nums`, compute `complement = target - num`.
- If `complement` is already in the map, return its index + current index.
- Else, add `num` and its index to the map.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

**Why this works:**  
Hash maps give us fast lookups. Instead of searching the entire array for the complement, we just peek into our map.
---

### 💡 Key Takeaways:

🧱 **Stack Mechanics:**  
Tracking extra info (like min) can supercharge standard data structures.

🧠 **Hash Maps:**  
 Hash maps are helpful in lookup-heavy problems.
