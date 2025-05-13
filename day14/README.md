# 🚀 Day 14 – #DrGViswanathan 50 Days Coding Challenge  
Today we’re working with partitioning linked lists and reversing 32-bit integers. 

## 💫 DSA Challenge: Partition List (LeetCode 86)  
Problem: Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x. You must preserve the original relative order of the nodes in each of the two partitions.

### Approach:  
- Use two dummy nodes to create two separate linked lists — one for nodes less than x, and one for nodes greater than or equal to x.  
-  Iterate through the original list and add each node to the appropriate list based on its value.  
-  Connect the end of the "less than x" list to the beginning of the "greater or equal to x" list.  
-  Make sure to set the end of the second list to None to avoid any dangling pointers or cycles.
  
Time Complexity: O(n), where n is the number of nodes in the list.  
Space Complexity: O(1) — extra space is only for pointers.    

Why this works: By preserving the original order within each partition and smartly using two separate chains, we achieve a clean and efficient solution with just one pass through the list.

## 💫 Math-based Challenge: Reverse Integer (LeetCode 7)  
Problem: Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [−2³¹, 2³¹ − 1], then return 0.

### Approach:  
-  Convert the absolute value of x to a string and reverse it.  
-  Keep track of the original sign and reapply it after the reversal.  
-  After reversing, check if the result is within the 32-bit signed integer range. If not, return 0.

  
Time Complexity: O(n), where n is the number of digits in x.  
Space Complexity: O(1), since we're not using any extra data structures beyond a few variables.  

Why this works: Rather than performing math-heavy reversal logic or risking 64-bit overflow, we take advantage of string reversal and strictly enforce 32-bit bounds.

## 💡 Key Takeaways:  
- Linked Lists: Using dummy nodes to build new linked list structures while preserving order is a powerful and reusable pattern.  
- Integers: Understanding constraints like integer size limits lets you solve problems with simple logic instead of brute force or unnecessary calculations. 

