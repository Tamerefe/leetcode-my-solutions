# LeetCode 3498 – Reverse Degree of a String

## Problem
[LeetCode #3498 – Reverse Degree of a String](https://leetcode.com/problems/reverse-degree-of-a-string/)

## Language
Java

## Approach
Each character is mapped to its position in the reversed alphabet:
`a -> 26`, `b -> 25`, ..., `z -> 1`.

For each index `i` (0-based), we compute:

`(reversed_value) * (i + 1)`

and sum over the entire string.

## Complexity
- Time: O(n)
- Space: O(1)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Feb 15, 2026 01:29  
> ⚙ Runtime: 1 ms  
> 🧠 Memory: 44.04 MB
