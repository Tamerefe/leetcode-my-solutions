# LeetCode 175 – Combine Two Tables

## Problem
[LeetCode #175 – Combine Two Tables](https://leetcode.com/problems/combine-two-tables/)

## Language
MySQL

## Approach
Use a `LEFT JOIN` to combine the `Person` and `Address` tables
based on `personId`.

This ensures that all records from `Person` are included,
even if there is no matching row in `Address`.

## Complexity
- Time: O(n)
- Space: O(1)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Feb 20, 2026 15:52  
> ⚙ Runtime: 361 ms