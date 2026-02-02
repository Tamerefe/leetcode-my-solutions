# LeetCode 2396 – Strictly Palindromic Number

## Problem
[LeetCode #2396 – Strictly Palindromic Number](https://leetcode.com/problems/strictly-palindromic-number/)

## Language
JavaScript

## Approach
For any integer `n >= 4`, its representation in base `n - 2` is always `12`,
which is not a palindrome. Therefore, no such `n` can satisfy the requirement
of being palindromic in every base from `2` to `n - 2`, so the answer is always `false`.

## Complexity
- Time: O(1)
- Space: O(1)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Feb 02, 2026 20:35  
> ⚙ Runtime: 0 ms  
> 🧠 Memory: 54.37 MB