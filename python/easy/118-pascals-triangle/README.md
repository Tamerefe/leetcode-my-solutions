# LeetCode 118 – Pascal's Triangle

## Problem
[LeetCode #118 – Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)

## Language
Python

## Approach
Build the triangle row by row.
- Each row starts and ends with `1`.
- Each inner element is the sum of the two elements above it:
  `arr[i-1][j-1] + arr[i-1][j]`.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Feb 16, 2026 16:04  
> ⚙ Runtime: 0 ms  
> 🧠 Memory: 18.80 MB
