# LeetCode 13 – Roman to Integer

## Problem
[LeetCode #13 – Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

## Language
Python

## Approach
The solution iterates through the Roman numeral string from left to right.
If the value of the current symbol is smaller than the next one, it is subtracted;
otherwise, it is added to the total.
Finally, the value of the last symbol is added to complete the conversion.

## Complexity
- Time: O(n)
- Space: O(1)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Feb 01, 2026 20:47  
> ⚙ Runtime: 10 ms  
> 🧠 Memory: 19.40 MB