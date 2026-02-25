# LeetCode 47 – Permutations II

## Problem
[LeetCode #47 – Permutations II](https://leetcode.com/problems/permutations-ii/)

## Language
Python

## Approach
Generate all permutations using `itertools.permutations`
and remove duplicates by converting the result to a `set`.

## Complexity
- Time: O(n! * n)
- Space: O(n!)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Feb 25, 2026 17:30  
> ⚙ Runtime: 7 ms  
> 🧠 Memory: 19.56 MB