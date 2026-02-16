# LeetCode 119 – Pascal's Triangle II

## Problem
[LeetCode #119 – Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/)

## Language
Python

## Approach
Generate Pascal's triangle row by row up to `rowIndex`,
then return the last generated row.

Each row starts and ends with `1`.
Inner values are computed using:
`arr[i-1][j-1] + arr[i-1][j]`.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Feb 16, 2026 16:51  
> ⚙ Runtime: 0 ms  
> 🧠 Memory: 19.46 MB
