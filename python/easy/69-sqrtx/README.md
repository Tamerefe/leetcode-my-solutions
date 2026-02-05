# LeetCode 69 – Sqrt(x)

## Problem
[LeetCode #69 – Sqrt(x)](https://leetcode.com/problems/sqrtx/)

## Language
Python

## Approach
This solution uses Newton's method to approximate `sqrt(x)`.
Starting from an initial guess, the estimate is updated with:

`n = (n + x / n) / 2`

The loop stops when the integer part of the estimate no longer changes,
which yields the required floor value.

## Complexity
- Time: O(log x) (fast convergence in practice)
- Space: O(1)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Feb 06, 2026 00:34  
> ⚙ Runtime: 3 ms  
> 🧠 Memory: 19.72 MB