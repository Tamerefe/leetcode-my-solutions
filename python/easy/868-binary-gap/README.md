# LeetCode 868 – Binary Gap

## Problem
[LeetCode #868 – Binary Gap](https://leetcode.com/problems/binary-gap/)

## Language
Python

## Approach
1. Convert the number to binary.
2. Store the indexes of all `'1'` bits.
3. Compute distances between consecutive `'1'` positions.
4. Return the maximum distance.

If there are fewer than two `1`s, return 0.

## Complexity
- Time: O(log n)
- Space: O(log n)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Feb 22, 2026 17:20  
> ⚙ Runtime: 0 ms  
> 🧠 Memory: 19.58 MB