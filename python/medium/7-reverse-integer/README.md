# LeetCode 7 – Reverse Integer

## Problem
[LeetCode #7 – Reverse Integer](https://leetcode.com/problems/reverse-integer/)

## Language
Python

## Approach
Reverse the integer by converting it to a string and reversing it.
Handle negative numbers separately.

After reversing, check if the result fits within the 32-bit signed integer range:
- `[-2^31, 2^31 - 1]`

If it overflows, return `0`.

## Complexity
- Time: O(log n)
- Space: O(log n)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Mar 15, 2026 15:02  
> ⚙ Runtime: 46 ms  
> 🧠 Memory: 19.05 MB