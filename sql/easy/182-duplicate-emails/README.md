# LeetCode 182 – Duplicate Emails

## Problem
[LeetCode #182 – Duplicate Emails](https://leetcode.com/problems/duplicate-emails/)

## Language
MySQL

## Approach
Group rows by `email` and filter using `HAVING COUNT(*) > 1`
to return emails that appear more than once.

## Complexity
- Time: O(n)
- Space: O(1)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Feb 20, 2026 16:12  
> ⚙ Runtime: 351 ms