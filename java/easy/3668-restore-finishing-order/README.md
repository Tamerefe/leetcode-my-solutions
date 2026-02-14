# LeetCode 3668 – Restore Finishing Order

## Problem
[LeetCode #3668 – Restore Finishing Order](https://leetcode.com/problems/restore-finishing-order/)

## Language
Java

## Approach
Traverse `order` and keep the elements that also appear in `friends`,
preserving the original order from `order`.

## Complexity
- Time: O(n * m)
- Space: O(n)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Feb 15, 2026 00:59  
> ⚙ Runtime: 1 ms  
> 🧠 Memory: 46.86 MB