# 🚀 Day 12 – #DrGViswanathan 50 Days Coding Challenge

Another day, another set of challenges. Let's dive right in! 🚀

---

## 💫 DSA Challenge: Insert Greatest Common Divisors (LeetCode 2807)
**Problem:** Given the head of a singly linked list, insert a new node with the greatest common divisor (GCD) between every pair of adjacent nodes. 

### Approach:
1. **Traverse the List:** Iterate through the list using a pointer `current`.
2. **Calculate GCD:** For each pair of adjacent nodes, calculate the GCD of the values.
3. **Insert GCD Node:** Create a new node with the calculated GCD value and insert it between the two adjacent nodes.
4. **Continue Traversing:** Move to the next pair of nodes and repeat until the end of the list.

- **Time Complexity:** O(n), where `n` is the number of nodes in the list (one pass through the list).  
- **Space Complexity:** O(1) additional space for the new nodes inserted.  
- **Why this works:** This method effectively integrates the calculated GCD between adjacent nodes while maintaining the original list structure.

---

## 💫 Math-based Challenge: Count Odd Numbers in an Interval Range (LeetCode 1523)
**Problem:** Given two integers `low` and `high`, return the count of odd numbers in the inclusive range from `low` to `high`.

### Approach:
1. **Odd Count Calculation:** 
   - To count odd numbers in a range, we leverage the fact that odd numbers are spaced evenly every 2 numbers.
   - Use integer division to determine how many odd numbers fall in the range `[low, high]`.
   
2. **Formula:** The number of odd numbers from `low` to `high` is given by `(high + 1) // 2 - low // 2`.

- **Time Complexity:** O(1)  
- **Space Complexity:** O(1)  
- **Why this works:** By using simple integer division, we directly calculate the count of odd numbers without needing to iterate through the entire range.

---

## 💡 Key Takeaways:
- **Linked Lists:** Inserting elements based on calculations like GCD can be a useful technique for manipulating list structures dynamically.
- **Math Problems:** Sometimes, the solution lies in finding a clean mathematical formula to avoid unnecessary iterations, making the solution both time and space efficient.

