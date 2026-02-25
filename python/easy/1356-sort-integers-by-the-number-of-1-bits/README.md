# LeetCode 1356 – Sort Integers by The Number of 1 Bits

## Problem
[LeetCode #1356 – Sort Integers by The Number of 1 Bits](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/)

## Language
Python

## Approach
Manually insert each number into a new list
based on the tuple comparison:

(bit_count, number)

This ensures:
1. Sort by number of 1 bits
2. If equal, sort by numeric value

## Complexity
- Time: O(n^2)
- Space: O(n)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Feb 25, 2026 15:10  
> ⚙ Runtime: 125 ms  
> 🧠 Memory: 19.53 MB