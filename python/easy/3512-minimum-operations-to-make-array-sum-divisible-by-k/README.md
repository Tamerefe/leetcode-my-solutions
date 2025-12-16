# LeetCode 3512 – Minimum Operations to Make Array Sum Divisible by K

## Problem
[LeetCode #3512 – Minimum Operations to Make Array Sum Divisible by K](https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/)

## Language
Python

## Approach
Each operation decreases the total sum by one.
To make the sum divisible by `k`, we compute the remainder of the sum modulo `k`
and determine the minimum number of decrements needed.

## Complexity
- Time: O(n)
- Space: O(1)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Dec 17, 2025 01:15  
> ⚙ Runtime: 3 ms  
> 🧠 Memory: 18.07 MB