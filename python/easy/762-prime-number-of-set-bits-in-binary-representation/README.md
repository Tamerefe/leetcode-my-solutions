# LeetCode 762 – Prime Number of Set Bits in Binary Representation

## Problem
[LeetCode #762 – Prime Number of Set Bits in Binary Representation](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/)

## Language
Python

## Approach
For each number in the range `[left, right]`:
1. Count the number of set bits (`1`s) in its binary form.
2. Check if that count is a prime number.
3. Increment the result if prime.

## Complexity
- Time: O(n log n)
- Space: O(1)

## Implementation Notes
> 🟢 **Accepted**  
> 🕒 Submitted at Feb 21, 2026 13:16  
> ⚙ Runtime: 143 ms  
> 🧠 Memory: 19.52 MB