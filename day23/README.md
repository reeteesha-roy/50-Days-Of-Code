🚀 Day 23 – #DrGViswanathan 50 Days Coding Challenge  
Today’s challenges focused on binary search precision and navigating well-formed strings — two fundamental concepts in algorithmic thinking.

---

💫 Array Challenge: Search Insert Position (LeetCode 35)  
**Problem:**  
Given a sorted array of distinct integers and a target value, return the index if the target is found.  
If not, return the index where it would be inserted in order.

**Approach:**

- Use Binary Search:
  - Initialize `left` and `right` pointers.
  - Find the middle element.
  - If target equals mid, return mid.
  - If target < mid, search left half.
  - If target > mid, search right half.
- If not found, return `left` as the correct insert position.

**Time Complexity:** O(log n)  
**Space Complexity:** O(1)

**Why this works:**  
Binary search halves the search space at each step, making it an efficient choice for sorted arrays.

---

💫 String Challenge: Longest Valid Parentheses (LeetCode 32)  
**Problem:**  
Given a string containing just the characters `'('` and `')'`, return the length of the longest valid (well-formed) parentheses substring.

**Approach:**

- Use a stack to track indices.
- Initialize stack with `-1` to handle base case.
- Iterate through the string:
  - Push index if `'('`
  - If `')'`, pop from the stack:
    - If stack is empty, push current index as new base.
    - Else, calculate length as `i - stack[-1]` and update max.
- Return the max length found.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

**Why this works:**  
Tracking unmatched parentheses with indices allows us to efficiently compute the maximum valid substring length in one pass.

---

💡 Key Takeaways:

- Binary search is the go-to for O(log n) insert/find operations in sorted data.
- Using a stack to track character positions makes validating and parsing parentheses-based strings both fast and intuitive.

