# 🚀 Day 45 – #DrGViswanathan 50 Days Coding Challenge

Today's problems explored graph theory fundamentals and string mathematics, demonstrating trust relationships in directed graphs and mathematical properties of string repetition patterns.

---

## 💫 Graph Challenge: Find the Town Judge (LeetCode 997)

**Problem:**  
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge. The town judge trusts nobody, and everybody (except for the town judge) trusts the town judge. Return the label of the town judge if they exist and can be identified uniquely, otherwise return -1.

**Approach:**  
Use indegree and outdegree counting:
1. Create arrays to track trust relationships: `trustCount` for incoming trust, `trusted` for outgoing trust.
2. For each trust relationship `[a, b]`, increment `trustCount[b]` and `trusted[a]`.
3. The judge must have `trustCount[judge] = n-1` (everyone trusts them) and `trusted[judge] = 0` (trusts nobody).
4. Alternatively, use a single array where `score[i] = trustCount[i] - trusted[i]`.

**Time Complexity:** O(n + t), where t is the number of trust relationships  
**Space Complexity:** O(n)

**Why this works:**  
The judge has unique properties: maximum incoming trust (n-1) and zero outgoing trust. By tracking these metrics, we can identify the judge or determine if no such person exists.

---

## 💫 String Challenge: Greatest Common Divisor of Strings (LeetCode 1071)

**Problem:**  
For two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`. A string `x` divides string `s` if `s` can be constructed by concatenating `x` one or more times.

**Approach:**  
Use mathematical GCD principle with string validation:
1. First check if `str1 + str2 == str2 + str1`. If not, no common divisor exists.
2. Find the GCD of the lengths of both strings using Euclidean algorithm.
3. The GCD string is the prefix of either string with length equal to the GCD of lengths.
4. Verify that this prefix actually divides both strings.

**Time Complexity:** O(n + m), where n and m are the lengths of the strings  
**Space Complexity:** O(1)

**Why this works:**  
If two strings have a common divisor, then concatenating them in either order produces the same result. The length of the largest common divisor must be the GCD of their individual lengths, following mathematical principles applied to strings.

---

## 💡 Key Takeaways:
- Graph problems often involve analyzing node relationships through degree counting and constraint satisfaction.
- String divisibility problems can leverage mathematical GCD concepts when combined with proper validation checks.
