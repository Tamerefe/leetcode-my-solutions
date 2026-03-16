# LeetCode 1431 – Kids With the Greatest Number of Candies

## Problem
[LeetCode #1431 – Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)

## Language
Python

## Approach
1. Find the maximum number of candies any kid currently has.
2. For each kid, check if adding `extraCandies` would make their total
   greater than or equal to the current maximum.
3. Return a list of boolean values.

## Complexity
- Time: O(n)
- Space: O(n)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Mar 16, 2026 13:35  
> ⚙ Runtime: 2 ms  
> 🧠 Memory: 19.26 MB