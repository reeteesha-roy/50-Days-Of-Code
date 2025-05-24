# 🚀 Day 25 – #DrGViswanathan 50 Days Coding Challenge

Today’s problems involved array manipulation and implementing stack behavior using basic queue operations.


---

## 💫 Array Challenge: Rotate Array (LeetCode 189)

**Problem:**  
Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

**Approach:**  
Use the reverse method:
1. Reverse the entire array  
2. Reverse the first `k` elements  
3. Reverse the rest  

This keeps everything in-place with no extra space.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)  

**Why this works:**  
Reversing cleverly reorders elements to simulate rotation. It's optimal and elegant.

---

## 💫 Stack Challenge: Implement Stack using Queues (LeetCode 225)

**Problem:**  
Implement a last-in-first-out (LIFO) stack using only two queues. Support `push`, `pop`, `top`, and `empty`.

**Approach:**  
Use two queues. On `push`, insert into the empty queue and move all old elements behind the new one to maintain LIFO order.

**Time Complexity:**  
- `push`: O(n)  
- `pop`, `top`, `empty`: O(1)

**Space Complexity:** O(n)  

**Why this works:**  
You simulate stack behavior with queues by controlling the order of elements. Smart use of data structure properties!

---

## 💡 Key Takeaways:

- In-place algorithms are game-changers for space optimization.  
- You can simulate any data structure with others if you understand their core mechanics.  
- Think reverse, not brute-force. Think queues, not just stacks.


