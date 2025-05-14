# 🚀 Day 15 – #DrGViswanathan 50 Days Coding Challenge  
Today, we tackle problems related to finding the longest substring without repeating characters and converting a given integer to its corresponding Excel column title. Let’s dive into these challenges!

## 💫 DSA Challenge: Longest Substring Without Repeating Characters (LeetCode 3)  
**Problem:** Given a string `s`, find the length of the longest substring without repeating characters.

### Approach:
- Use a sliding window technique with two pointers, `left` and `right`.
- Keep track of the characters in the current window using a dictionary or hash map.
- As you iterate through the string with the `right` pointer, check if the character at `right` is already in the current window.
- If it is, move the `left` pointer to the right of the first occurrence of the repeated character to maintain the uniqueness of the substring.
- Keep track of the maximum length encountered during this process.

**Time Complexity:** O(n), where n is the length of the string.  
**Space Complexity:** O(min(n, m)), where n is the length of the string and m is the size of the character set.

**Why this works:** By dynamically adjusting the window to always contain unique characters, we efficiently find the longest substring without duplicates using just a single pass through the string.

## 💫 Math-based Challenge: Convert Integer to Excel Column Title (LeetCode 168)  
**Problem:** Given an integer `columnNumber`, return its corresponding column title as it appears in an Excel sheet.

### Approach:
- Think of the column number in a base-26 system, but adjust for the fact that Excel columns are 1-indexed.
- Repeatedly divide the `columnNumber` by 26 to get the corresponding character for the current "digit" in the column title.
- For each division, find the remainder, which corresponds to a letter (A-Z).
- After finding the corresponding letter, update `columnNumber` and repeat the process until the entire title is constructed.
  
**Time Complexity:** O(log n), where n is the column number.  
**Space Complexity:** O(1) — no extra space is needed apart from a few variables for the process.

**Why this works:** By handling the column number similarly to a base-26 system while accounting for 1-based indexing, we can map numbers to their Excel column titles efficiently.

## 💡 Key Takeaways:  
- **Sliding Window:** A powerful technique to solve problems involving substrings or subarrays while maintaining certain constraints (like uniqueness).  
- **Base Conversion:** Understanding how to convert between number systems (like base-10 to base-26) and how it relates to real-world problems (like Excel columns) can help simplify complex tasks.

