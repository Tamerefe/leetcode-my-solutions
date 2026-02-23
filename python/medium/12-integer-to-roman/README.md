# LeetCode 12 – Integer to Roman

## Problem
[LeetCode #12 – Integer to Roman](https://leetcode.com/problems/integer-to-roman/)

## Language
Python

## Approach
Break the number into digits and process each digit according to its place value:
- Units
- Tens
- Hundreds
- Thousands

Use Roman numeral symbol groups `(one, five, ten)` for each position.
Construct the result from right to left.

## Complexity
- Time: O(1)
- Space: O(1)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Feb 23, 2026 18:46  
> ⚙ Runtime: 4 ms  
> 🧠 Memory: 19.31 MB