# LeetCode 8 – String to Integer (atoi)

## Problem
[LeetCode #8 – String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

## Language
JavaScript

## Approach
1. Trim leading whitespace.
2. Use regex `^[+-]?\d+` to extract the valid integer prefix.
3. Convert the result to a number.
4. Clamp the value within 32-bit signed integer range:
   `[-2^31, 2^31 - 1]`.

## Complexity
- Time: O(n)
- Space: O(1)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Mar 18, 2026 15:55  
> ⚙ Runtime: 1 ms  
> 🧠 Memory: 57.63 MB