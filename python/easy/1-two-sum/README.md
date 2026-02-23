# LeetCode 1 – Two Sum

## Problem
[LeetCode #1 – Two Sum](https://leetcode.com/problems/two-sum/)

## Language
Python

## Approach
Use two nested loops and check every pair `(i, j)` such that:
- `i < j`
- `nums[i] + nums[j] == target`

Return the indices when a match is found.

## Complexity
- Time: O(n^2)
- Space: O(1)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Feb 23, 2026 16:03  
> ⚙ Runtime: 1752 ms  
> 🧠 Memory: 19.90 MB