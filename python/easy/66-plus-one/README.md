# LeetCode 66 – Plus One

## Problem
[LeetCode #66 – Plus One](https://leetcode.com/problems/plus-one/)

## Language
Python

## Approach
Traverse the array from right to left.
- If a digit is not 9, increment it and stop.
- If it is 9, set it to 0 and continue carrying.
If all digits become 0, insert 1 at the front.

## Complexity
- Time: O(n)
- Space: O(1)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Feb 16, 2026 15:07  
> ⚙ Runtime: 0 ms  
> 🧠 Memory: 19.07 MB
