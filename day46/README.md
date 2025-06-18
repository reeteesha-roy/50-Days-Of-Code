# 🚀 Day 46 – #DrGViswanathan 50 Days Coding Challenge

Today's problems involved graph analysis and number theory, showcasing star graph identification and prime number mathematical properties combined with palindrome validation.

---

## 💫 Graph Challenge: Find Center of Star Graph (LeetCode 1791)

**Problem:**  
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node. Return the center of the given star graph.

**Approach:**  
Use edge frequency analysis:
1. In a star graph, the center node appears in every edge.
2. **Method 1 - Count Degrees:** Count the degree of each node; the center has degree n-1.
3. **Method 2 - First Two Edges:** Check the first two edges. The common node between them is the center.
4. **Method 3 - Hash Map:** Count occurrences of each node; the one appearing n-1 times is the center.

**Time Complexity:** O(1) for Method 2, O(n) for other methods  
**Space Complexity:** O(1) for Method 2, O(n) for hash map method

**Why this works:**  
In a star graph, only the center node connects to all other nodes. By checking just the first two edges, we can identify the center immediately since it must be the common node between any two edges.

---

## 💫 Number Theory Challenge: Prime Palindromes (LeetCode 762)

**Problem:**  
Given an integer n, return the smallest prime number that is greater than or equal to n, and is also a palindrome.

**Approach:**  
Use mathematical optimization with palindrome properties:
1. **Key Insight:** All even-length palindromes (except 11) are divisible by 11, so they can't be prime.
2. Generate odd-length palindromes by taking a number and mirroring it.
3. For each candidate palindrome ≥ n, check if it's prime.
4. **Optimization:** Start from the appropriate half-length number and build palindromes.

**Time Complexity:** O(√p), where p is the result prime  
**Space Complexity:** O(1)

**Why this works:**  
Mathematical property: even-length palindromes have alternating digit sum patterns that make them divisible by 11. By focusing on odd-length palindromes and using efficient primality testing, we can find the answer without checking every number.

---

## 💡 Key Takeaways:
- Star graphs have unique structural properties that allow for constant-time center identification using minimal edge information.
- Number theory problems often benefit from mathematical insights that eliminate large search spaces through divisibility rules.
