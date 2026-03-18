# LeetCode 21 – Merge Two Sorted Lists

## Problem
[LeetCode #21 – Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

## Language
Java

## Approach
Use a dummy node to build the merged list.

- Compare nodes from both lists
- Attach the smaller node to the result
- Move pointers forward
- When one list ends, attach the remaining part of the other list

## Complexity
- Time: O(n + m)
- Space: O(1)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Mar 18, 2026 15:37  
> ⚙ Runtime: 0 ms  
> 🧠 Memory: 44.16 MB