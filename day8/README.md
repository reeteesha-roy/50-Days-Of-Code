# 🚀 Day 8 – #DrGViswanathan 50 Days Coding Challenge

Today’s lineup: list restructuring based on node index parity and decoding spreadsheet columns like a boss. 📊🧮

---

## 💫 DSA Challenge: Odd Even Linked List (LeetCode 328)
**Problem:** Rearrange a linked list so that all odd-indexed nodes come before even-indexed ones (1-based indexing).

### Approach:
1. **Edge handling:** Early return if the list is empty or has only one node.
2. **Split the list into two:** 
   - `odd` list starting from head.
   - `even` list starting from head.next.
3. **Traverse and re-link:**
   - Link odd nodes together skipping one each time.
   - Same for even nodes.
4. **Reattach:** Link the tail of the odd list to the head of the even list.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)  
- **Why this works:** Pure pointer manipulation — no extra space, no fancy data structures. Just clean restructuring based on index parity.

---

## 💫 Math-based Challenge: Excel Sheet Column Number (LeetCode 171)
**Problem:** Convert a spreadsheet column title (e.g., "AB") to its corresponding column number.

### Approach:
Treated it like a **base-26 number system** where:
- `'A'` = 1, `'B'` = 2, ..., `'Z'` = 26.
- Iterated through each character:
  - Multiplied the current result by 26.
  - Added the value of the current character.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)  
- **Why this works:** It's like parsing a base-10 number — just with 26 instead. Super efficient, super clean.

---

## 💡 Key Takeaways:
- **Linked Lists:** Splitting and stitching with pointer gymnastics can achieve surprisingly elegant reorders.
- **Math Logic:** Understanding number systems (like base-26) opens doors to intuitive decoding.

